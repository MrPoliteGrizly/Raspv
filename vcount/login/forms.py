# -*- coding: utf-8 -*-
'''
Created on 31.07.2013

@author: alexander.kozlov@itseez.com
'''

from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=20, required=False)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(), required=False)
    
    def clean_login(self):
        login = self.cleaned_data['login']
        
        if not login:
            login = ''
        
        return login
    
    def clean_password(self):
        password = self.cleaned_data['password']
        
        if not password:
            password = ''
        
        return password