'''
Created on 12.08.2013

@author: alexander.kozlov@itseez.com
'''

from django import forms
import re
from vCountDjGui.auxilary import getPageString

class UpdateForm(forms.Form):
    filename  = forms.FileField()
    
    def __init__(self, language='rus', *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.language = language
