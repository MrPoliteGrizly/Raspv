# -*- coding: utf-8 -*-
'''
Created on 13.08.2013

@author: alexander.kozlov@itseez.com
'''
from django import forms
from vCountDjGui.auxilary import getPageString

class PasswordForm(forms.Form):
    oldpassword = forms.CharField(widget = forms.PasswordInput(), required = False)
    newpassword = forms.CharField(widget = forms.PasswordInput(), required = False)
    newrepeatedpassword = forms.CharField(widget = forms.PasswordInput(), required = False)
    
    def __init__(self, language='rus', *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.language = language

    def clean_oldpassword(self):
        oldpasswordtext = self.cleaned_data['oldpassword']
        
        if not oldpasswordtext:
            raise forms.ValidationError(getPageString('passwordForm', 'incorrectOldPassword', self.language))
        
        return oldpasswordtext
    
    def clean_newpassword(self):
        newpassword = self.cleaned_data['newpassword']
        
        if not newpassword:
            raise forms.ValidationError(getPageString('passwordForm', 'incorrectNewPassword', self.language))
        
        return newpassword
    
    def clean_newrepeatedpassword(self):
        newrepeatedpassword = self.cleaned_data['newrepeatedpassword']
        
        if not newrepeatedpassword:
            raise forms.ValidationError(getPageString('passwordForm', 'incorrectRepeatedPassword', self.language))
        
        return newrepeatedpassword