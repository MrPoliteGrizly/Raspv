# -*- coding: utf-8 -*-
# Create your views here.
from password.forms import *
from password.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vCountDjGui.auxilary import isLoggedIn, closeSession, getLanguageByRequest, getPageDictionary, getErrorList
from vCountDjGui.auxilary import rootDir 
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
    dictum = getPageDictionary(request, 'passwordForm')
    lang = getLanguageByRequest(request)
    
    if request.method == 'POST':
        form = PasswordForm(language=lang, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result, reason = setPassword(cd, lang)
            if result:
                return HttpResponse(dictum['passwordChangedMessage'])
            else:
                return HttpResponse(reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], getErrorList('%s' % form.errors)))
    else:
        passwordform = PasswordForm(language=lang)
    
    
    return render(request, 'password/password_form.html', {'form' : passwordform, 'dictum': dictum})