# -*- coding: utf-8 -*-
# Create your views here.

from settings.models import *
from administration.forms import *
from administration.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vCountDjGui.auxilary import isLoggedIn, closeSession, getPageDictionary, getLanguageByRequest, getErrorList

def index(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    hostnameform = HostNameForm(initial=getHNFormInitials())
    datetimefrom = DateTimeForm(initial=getDateTimeFormInitials())
    logsform = LogsForm()
    resenddataform = ResendDataForm(initial=resendateFormInitials())
    notificationsform = NotificationsForm(initial=notificationsInitials())
    networkform = NetworkForm(initial=getIpConfigInitials())
    dictum = getPageDictionary(request, 'administrationForm')
    
    return render(request, 'administration/administration_forms.html', {'hostnameform' : hostnameform, 'datetimefrom' : datetimefrom,
                                                                        'logsform': logsform, 'resenddataform' : resenddataform,
                                                                        'notificationsform' : notificationsform, 'networkform' : networkform,
                                                                        'dictum': dictum})

def changeHostName(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'administrationForm')
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = HostNameForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setHostName(cd)
            if result:
                return HttpResponse(dictum['hostnameChangeMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        redirect('/administration/')
        
def changeDateTime(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'administrationForm')
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = DateTimeForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setDateTime(cd)
            if result:
                return HttpResponse(dictum['datetimeChangeMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        redirect('/administration/')
        
def sendLogs(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'administrationForm')
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = LogsForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setLogsEmail(cd)
            if result:
                return HttpResponse(dictum['logsSendMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        redirect('/administration/')
        
def resendData(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'administrationForm')
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = ResendDataForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setResendData(cd)
            if result:
                return HttpResponse(dictum['dataSendMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        redirect('/administration/')
        
def setNotifications(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'administrationForm')
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = NotificationsForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setNotificationsSettings(cd)
            if result:
                return HttpResponse(dictum['settingsSavedMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        redirect('/administration/')
        
def setNetwork(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'administrationForm')
    if request.method == 'POST':
        lang = getLanguageByRequest(request)
        form = NetworkForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setNetworkSettings(cd)
            if result:
                return HttpResponse(dictum['settingsSavedMessage'])
            else:
                return HttpResponse('Error! ' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        redirect('/administration/')