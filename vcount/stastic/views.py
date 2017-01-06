# Create your views here.
from settings.models import ServiceSettings
from channels.models import *
from channels.forms import ChannelsForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vCountDjGui.auxilary import isLoggedIn, closeSession, getPageDictionary
from chartit import DataPool, Chart

def index(request):
    '''if not isLoggedIn(request):
        return redirect('/login/')'''
    
    settings = ServiceSettings()
    dictum = getPageDictionary(request, 'stasticForm') 
    
    if request.method == 'POST':
        form = ChannelsForm(request.POST)
        if form.is_valid():
            result, reason = setSettingsToXML(form, settings)
            if result:
                return HttpResponse(dictum['settingsSavedMessage'])
            else:
                return HttpResponse('Server error!' + reason)
        else:
            return HttpResponse('%s\n %s' % (dictum['formErrors'], form.errors))
    
    initialVals = setSettingsToView(settings)
    form = ChannelsForm(initial=initialVals)
    
    return render(request, 'stastic/stastic_form.html', {'form': form, 'dictum': dictum})


