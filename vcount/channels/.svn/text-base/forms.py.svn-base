'''
Created on 07.08.2013

@author: alexander.kozlov@itseez.com
'''
from django import forms

class ChannelsForm(forms.Form):
    ignoredcells = forms.CharField(max_length=1000, widget = forms.HiddenInput())
    y_offset1 = forms.CharField(max_length=5, widget = forms.HiddenInput())
    y_offset2 = forms.CharField(max_length=5, widget = forms.HiddenInput())
    minflow = forms.CharField(max_length=10, widget = forms.HiddenInput())
    maxflow = forms.CharField(max_length=10, widget = forms.HiddenInput())
    
    isswitched = forms.BooleanField(required=False)
    savevideo = forms.BooleanField(required=False)
    useautocalibration = forms.BooleanField(required=False)