'''
Created on 08.08.2013

@author: alexander.kozlov@itseez.com
'''
from django import forms
from administration.models import getWifiEssids
from vCountDjGui.auxilary import getPageString
import re

#getPageString('settingsForm', stringID, self.language)

class HostNameForm(forms.Form):
    hostname = forms.CharField(max_length=30, required = False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(HostNameForm, self).__init__(*args, **kwargs)
        self.language = language

    def clean_hostname(self):
        expr = re.compile(r'^([A-Za-z0-9._%+-]+){2,}$')
        hostname = self.cleaned_data['hostname']
        
        if not hostname or not bool(expr.match(hostname)):
            raise forms.ValidationError(getPageString('administrationForm', 'hostnameError', self.language))
        
        return hostname
    
class DateTimeForm(forms.Form):
    datetimefield = forms.CharField(max_length=22, required = False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(DateTimeForm, self).__init__(*args, **kwargs)
        self.language = language

    def clean_datetimefield(self):
        expr = re.compile(r'^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] ([01]?[0-9]|2[0-3]):[0-5][0-9]$')
        datetimefield = self.cleaned_data['datetimefield']
        
        if not datetimefield or not bool(expr.match(datetimefield)):
            raise forms.ValidationError(getPageString('administrationForm', 'datetimefieldError', self.language))
        
        return datetimefield
    
class LogsForm(forms.Form):
    emailto = forms.CharField(max_length=100)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(LogsForm, self).__init__(*args, **kwargs)
        self.language = language

    def clean_emailto(self):
        expr = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9\-.-]+\.[A-Za-z]{2,}$')
        emailto = self.cleaned_data['emailto']
        
        if not bool(expr.match(emailto)):
            raise forms.ValidationError(getPageString('administrationForm', 'emailtoError', self.language))
        
        return emailto
    
class ResendDataForm(forms.Form):
    CHOICES = (('1', 'All',), ('2', 'Choose date',))
    resendtype = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial='1', required = True)
    resenddate = forms.CharField(max_length=22, required=False)#forms.DateTimeField(input_formats=('%Y-%m-%d %H:%M',), required=False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(ResendDataForm, self).__init__(*args, **kwargs)
        self.language = language

    def clean_resenddate(self):
        expr = re.compile(r'^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] ([01]?[0-9]|2[0-3]):[0-5][0-9]$')
        resenddate = self.cleaned_data['resenddate']
        
        if not resenddate or not bool(expr.match(resenddate)):
            raise forms.ValidationError(getPageString('administrationForm', 'datetimefieldError', self.language))
        
        return resenddate
    
class NotificationsForm(forms.Form):
    notify = forms.BooleanField(required=False)
    notificationemail = forms.CharField(max_length=100, required=False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(NotificationsForm, self).__init__(*args, **kwargs)
        self.language = language

    def clean_notificationemail(self):
        expr = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9\-.-]+\.[A-Za-z]{2,}$')
        notificationemail = self.cleaned_data['notificationemail']
        
        if notificationemail and not bool(expr.match(notificationemail)):
            raise forms.ValidationError(getPageString('administrationForm', 'emailtoError', self.language))
        
        return notificationemail
    

class NetworkForm(forms.Form):
    CHOICES = (('0', 'First',), ('1', 'Second',))
    networktype = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, required = True)
    wifipassword = forms.CharField(required=False, widget = forms.PasswordInput(render_value = True))
    iptype = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, required = True)
    ipaddress = forms.CharField(max_length=20, required=False)
    ipmask = forms.CharField(max_length=20, required=False)
    gateway = forms.CharField(max_length=20, required=False)
    dnsserver = forms.CharField(max_length=20, required=False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(NetworkForm, self).__init__(*args, **kwargs)
        self.fields['wifiessid'] = forms.ChoiceField(choices=getWifiEssids(), required = False)
        self.language = language
        
    def clean_ipaddress(self):
        expr = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        ipaddress = self.cleaned_data['ipaddress']
        
        if ipaddress and not bool(expr.match(ipaddress)):
            raise forms.ValidationError(getPageString('administrationForm', 'ipaddressError', self.language))
        
        return ipaddress
    
    def clean_ipmask(self):
        expr = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        ipmask = self.cleaned_data['ipmask']
        
        if ipmask and not bool(expr.match(ipmask)):
            raise forms.ValidationError(getPageString('administrationForm', 'ipmaskError', self.language))
        
        return ipmask
    
    def clean_gateway(self):
        expr = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        gateway = self.cleaned_data['gateway']
        
        if gateway and not bool(expr.match(gateway)):
            raise forms.ValidationError(getPageString('administrationForm', 'gatewayError', self.language))
        
        return gateway
    
    def clean_dnsserver(self):
        expr = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
        dnsserver = self.cleaned_data['dnsserver']
        
        if dnsserver and not bool(expr.match(dnsserver)):
            raise forms.ValidationError(getPageString('administrationForm', 'dnsserverError', self.language))
        
        return dnsserver