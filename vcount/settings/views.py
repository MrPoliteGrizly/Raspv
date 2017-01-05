# -*- coding: utf-8 -*-
# Create your views here.

from settings.models import *
from settings.forms import SettingsForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vCountDjGui.auxilary import isLoggedIn, closeSession, getPageDictionary, getLanguageByRequest, getErrorList, getErrorList2
from django.views.decorators.csrf import csrf_protect


import base64
import os, time, sys
import shutil
import smtplib
import getpass, poplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import subprocess
import datetime


def index(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    settings = ServiceSettings()
    
    dictum = getPageDictionary(request, 'settingsForm') 
    
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = SettingsForm(language=lang, data=request.POST)
        if form.is_valid():
            result, reason = setSettingsToXML(form, settings)
            if result:
                return HttpResponse(dictum['settingsSavedMessage'])
            else:
                return HttpResponse('Server error!' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList2('%s' % form.errors, 'settingsForm', getLanguageByRequest(request))))
    
    initialVals = setSettingsToView(settings)
    form = SettingsForm(initial=initialVals)
    
    return render(request, 'settings/settings_form.html', {'form': form, 'dictum': dictum})


@csrf_protect
def testEmail(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'settingsForm')
    
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = SettingsForm(language=lang, data=request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            result, reason = sendMail(cd['emailfrom'], cd['emailto'], cd['smtpserver'], cd['smtpport'], cd['smtpuser'], 
                                      cd['smtppassword'], 'Test mail', 'This is test mail from shop: ' + cd['shopid'] + '.', cd['usessl'])
            if result:
                return HttpResponse(dictum['emailSentMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList2('%s' % form.errors, 'settingsForm', getLanguageByRequest(request))))
        
    return HttpResponse("Error: Use post to check!")

@csrf_protect
def testServer(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'settingsForm')
    
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = SettingsForm(language=lang, data=request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            result, reason = sendPing(cd['serveraddress'], cd['serverport'], cd['shopid'])
            if result:
                return HttpResponse(dictum['pingSentMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList2('%s' % form.errors, 'settingsForm', getLanguageByRequest(request))))
        
    return HttpResponse("Error: Use post to check!")

@csrf_protect
def testShare(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'settingsForm')
    
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = SettingsForm(language=lang, data=request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            result, reason = mountShare(cd['sharepath'], cd['shareuser'], cd['sharepassword'])
            if result:
                return HttpResponse(dictum['shareMountMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList2('%s' % form.errors, 'settingsForm', getLanguageByRequest(request))))
        
    return HttpResponse("Error: Use post to check!")

def sendMail(mail_from, mail_to, server, port, user, password, subject, text, use_ssl):
    result = False
    
    testmail = 'testmail.txt'
    with open(testmail, 'w') as the_file:
        the_file.write(text+ '\n')
    
    command = 'python /usr/local/bin/vcount/mailsender.py -f %s -t %s -h %s -p %s -u %s -k %s -s "%s" -i "%s"' % (mail_from, mail_to, server, port, user, password, subject, testmail)
    
    if (use_ssl):
        command = command + ' -ssl'
    
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    
    if (p.returncode == 0):
        result = True
    
    out = out + err    
    
    return result, out

def sendMail2(mail_from, mail_to, server, port, user, password, subject, text, use_ssl):
    result = False
    reason = ''
    
    try:
        msg = MIMEMultipart()
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg['Subject'] = subject
    
        if (text != ""):
            msg.attach( MIMEText(text, 'plain') )

        mailServer = smtplib.SMTP(server, int(port))
        mailServer.ehlo()
    
        if (use_ssl == "true"):
            mailServer.starttls()
            mailServer.ehlo()

        mailServer.login(user, password)
        mail_to = mail_to.split(',')
        mailServer.sendmail(mail_from, mail_to, msg.as_string())

        mailServer.close()
        result = True
        
    except Exception, e:
        reason = "Error while sending mail: %s" % e
        
    return result, reason

def sendPing(address, port, shopName):
    result = False
    
    cwd = os.getcwd()
    
    command = 'python /usr/local/bin/vcount/WcfClient.py -a %s -p %s -c status -s Avalible -n %s' % (address, port, shopName)
    
    
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    
    if (p.returncode == 0):
        result = True
    
    out = out + err    
    
    return result, out


def mountShare(path, user, password):
    result = False
    
    cwd = os.getcwd()
    
    command = '/usr/local/bin/vcount/mount.sh -r -s %s -u %s -p %s -m /usr/local/bin/vcount/share' % (path, user, password)
    
    
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    
    if (p.returncode == 0):
        try:
            testfile = '/usr/local/bin/vcount/share' + '/Test_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.time'
            with open(testfile, 'w') as fd:
                fd.write(datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '\n')
            result = True
        except Exception, e:
            out = "%s" % e
    
    out = out + err    
    
    return result, out