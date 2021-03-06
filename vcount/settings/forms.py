# -*- coding: utf-8 -*-
'''
Created on 22.07.2013

@author: alexander.kozlov@itseez.com
'''
from django import forms
import re
from vCountDjGui.auxilary import getPageString

class SettingsForm(forms.Form):
    shopid = forms.CharField(max_length=100)
    workallday = forms.BooleanField(required=False)
    worktimefrom = forms.CharField(max_length=2, required=False)
    worktimetill = forms.CharField(max_length=2, required=False)
    intervalhours = forms.CharField(max_length=2, required=False)
    ismanualhours = forms.BooleanField(required=False)
    manualhours = forms.CharField(max_length=100, required=False)
    is1C = forms.BooleanField(required=False)
    sendbyemail = forms.BooleanField(required=False)
    emailto = forms.CharField(max_length=200,required=False)
    sendtoserver = forms.BooleanField(required=False)
    serveraddress = forms.CharField(max_length=100, required=False)
    serverport = forms.CharField(max_length=5, required=False)
    useshared = forms.BooleanField(required=False)
    sharepath = forms.CharField(max_length=100, required=False)
    shareuser = forms.CharField(max_length=30, required=False)
    sharepassword = forms.CharField(required=False, widget = forms.PasswordInput(render_value = True))
    emailfrom = forms.CharField(max_length=100,required=False)
    smtpserver = forms.CharField(max_length=30, required=False)
    smtpport = forms.CharField(max_length=5, required=False)
    attemptstosend = forms.CharField(max_length=1, required=False)
    useauthentication = forms.BooleanField(required=False)
    smtpuser = forms.CharField(max_length=30, required=False)
    smtppassword = forms.CharField(required=False, widget = forms.PasswordInput(render_value = True))
    usessl = forms.BooleanField(required=False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.language = language
        
    def getFormString(self, stringID):
        return getPageString('settingsForm', stringID, self.language)
    
    ''' Validators '''
    
    def clean_manualhours(self):
        expr = re.compile(r'^(([01]?[0-9]|2[0-3]):[0-5][0-9]){1}(,\s?(([01]?[0-9]|2[0-3]):[0-5][0-9]))*$')
        manualhourstext = self.cleaned_data['manualhours']
        
        if not manualhourstext or not bool(expr.match(manualhourstext)):
            raise forms.ValidationError(self.getFormString('manualhoursError'))
        
        return manualhourstext
    
    def clean_shopid(self):
        expr = re.compile(r'^[a-zA-Z0-9-_]+$')
        shopid = self.cleaned_data['shopid']
        
        if not bool(expr.match(shopid)):
            raise forms.ValidationError(self.getFormString('shopidError'))
        
        return shopid
    
    def clean_worktimefrom(self):
        expr = re.compile(r'^([01]?[0-9]|2[0-3])$')
        worktimefrom = self.cleaned_data['worktimefrom']
        
        if worktimefrom and not bool(expr.match(worktimefrom)):
            raise forms.ValidationError(self.getFormString('worktimefromError'))
        
        return worktimefrom
    
    def clean_worktimetill(self):
        expr = re.compile(r'^([01]?[0-9]|2[0-4])$')
        worktimetill = self.cleaned_data['worktimetill']
        
        if worktimetill and not bool(expr.match(worktimetill)):
            raise forms.ValidationError(self.getFormString('worktimetillError'))
        
        return worktimetill
    
    def clean_intervalhours(self):
        expr = re.compile(r'^([1-9]|2[0-4])$')
        intervalhours = self.cleaned_data['intervalhours']
        
        if not intervalhours or not bool(expr.match(intervalhours)):
            raise forms.ValidationError(self.getFormString('intervalhoursError'))
        
        return intervalhours
    
    def clean_emailto(self):
        expr = re.compile(r'^([A-Za-z0-9._%+-]+@[A-Za-z0-9\-.-]+\.[A-Za-z]{2,}){1}(,\s?([A-Za-z0-9._%+-]+@[A-Za-z0-9\-.-]+\.[A-Za-z]{2,}))*$')
        emailto = self.cleaned_data['emailto']
        
        if emailto and not bool(expr.match(emailto)):
            raise forms.ValidationError(self.getFormString('emailtoError'))
        
        emailto = emailto.replace(' ', '')
        return emailto
    
    def clean_serveraddress(self):
        expr = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        serveraddress = self.cleaned_data['serveraddress']
        
        if serveraddress and not bool(expr.match(serveraddress)):
            raise forms.ValidationError(self.getFormString('serveraddressError'))
        
        return serveraddress
    
    def clean_serverport(self):
        expr = re.compile(r'^(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3})$')
        serverport = self.cleaned_data['serverport']
        
        if serverport and not bool(expr.match(serverport)):
            raise forms.ValidationError(self.getFormString('serverportError'))
        
        return serverport
    
    def clean_sharepath(self):
        expr = re.compile(r'^//\w*(\.?\w*)*/(/?\w+)*/?$')
        sharepath = self.cleaned_data['sharepath']
        
        if sharepath and not bool(expr.match(sharepath)):
            raise forms.ValidationError(self.getFormString('sharepathError'))
        
        return sharepath
    
    def clean_shareuser(self):
        expr = re.compile(r'^[\w\.]+$')
        shareuser = self.cleaned_data['shareuser']
            
        if shareuser and not bool(expr.match(shareuser)):
            raise forms.ValidationError(self.getFormString('shareuserError'))
        
        return shareuser
    
    def clean_sharepassword(self):
        expr = re.compile(r'^[\w!@#\$\\]+$')
        sharepassword = self.cleaned_data['sharepassword']
            
        if sharepassword and not bool(expr.match(sharepassword)):
            raise forms.ValidationError(self.getFormString('sharepasswordError'))
        
        return sharepassword
    
    def clean_emailfrom(self):
        expr = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9\-.-]+\.[A-Za-z]{2,}$')
        emailfrom = self.cleaned_data['emailfrom']
        
        if emailfrom and not bool(expr.match(emailfrom)):
            raise forms.ValidationError(self.getFormString('emailfromError'))
        
        return emailfrom
    
    def clean_smtpserver(self):
        expr = re.compile(r'^[A-Za-z0-9._%+-]+\.[A-Za-z]{2,}$')
        smtpserver = self.cleaned_data['smtpserver']
        
        if smtpserver and not bool(expr.match(smtpserver)):
            raise forms.ValidationError(self.getFormString('smtpserverError'))
        
        return smtpserver
    
    def clean_smtpport(self):
        expr = re.compile(r'^(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3})$')
        smtpport = self.cleaned_data['smtpport']
        
        if smtpport and not bool(expr.match(smtpport)):
            raise forms.ValidationError(self.getFormString('smtpportError'))
        
        return smtpport
    
    def clean_attemptstosend(self):
        expr = re.compile(r'^\d$')
        attemptstosend = self.cleaned_data['attemptstosend']
        
        if attemptstosend and not bool(expr.match(attemptstosend)):
            raise forms.ValidationError(self.getFormString('attemptstosendError'))
        
        return attemptstosend
    
    def clean_smtpuser(self):
        expr = re.compile(r'^([A-Za-z0-9._%+-]+@[A-Za-z0-9\-.-]+\.[A-Za-z]{2,})|([A-Za-z0-9._%+-]+)$')
        smtpuser = self.cleaned_data['smtpuser']
        
        if smtpuser and not bool(expr.match(smtpuser)):
            raise forms.ValidationError(self.getFormString('smtpuserError'))
        
        return smtpuser