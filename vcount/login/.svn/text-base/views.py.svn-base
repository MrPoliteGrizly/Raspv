# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from login.models import verifyLogin
from login.forms import LoginForm
from vCountDjGui.auxilary import setLogin, getPageDictionary

def index(request):
    error = ''
    dictum = getPageDictionary(request, 'loginForm') 
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data 
            
            isCorrect, error = verifyLogin(cd['login'], cd['password'])
            if isCorrect:
                setLogin(request)
                return redirect('/')
            else:
                if not 'Server error' in error:
                    error = dictum[error]
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], form.errors))
            
                                
    form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form, 'error': error, 'dictum': dictum})