# -*- coding: utf-8 -*-
# Create your views here.
from settings.models import ServiceSettings
from channels.models import *
from channels.forms import ChannelsForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vCountDjGui.auxilary import isLoggedIn, closeSession, getPageDictionary
from qsstats import QuerySetStats
from datetime import date
from .models import Payment
from django.db.models import Count, Sum


def index(request):
    if not isLoggedIn(request):
        return redirect('/login/')
    
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

    start_date = date.today()
    end_date = date(2017, 2, 20)

    queryset = Payment.objects.all()
    # считаем количество платежей...
    qsstats = QuerySetStats(queryset, date_field='datetime', aggregate=Count('id'))
    # ...в день за указанный период
    values = qsstats.time_series(start_date, end_date, interval='days')
    # 2nd graph
    summary = qsstats.time_series(start_date, end_date, interval='days', aggregate=Sum('amount'))

    return render(request, 'stastic/stastic_form.html', {'form': form, 'dictum': dictum, 'values': values, 'summary': summary,})