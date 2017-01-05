# -*- coding: utf-8 -*-
'''
Created on 31.07.2013

@author: alexander.kozlov@itseez.com
'''

from django.shortcuts import redirect
from django.http import HttpResponse
from os.path import join, abspath, normpath, dirname
from vCountDjGui.languageprovider import LanguageMap, Dictionary, TabDictionary, CommonDictioanry
import xml.etree.ElementTree as ET
import sys

def isLoggedIn(request):
    result = False
    
    if request.session.has_key('authenticated') and request.session['authenticated']:
        result = True
    
    return result

def closeSession(request):
    request.session['authenticated'] = ''
    return redirect('/login/')
    
def setLogin(request):
    request.session['authenticated'] = 'True'
    
def changeLanguage(request):
    
    if request.method == 'POST':
        request.COOKIES['language'] = request.POST['language']
        
        nextPage = request.POST.get('next', None)
        if nextPage:
            response = redirect(nextPage)
            response.set_cookie( 'language', request.POST['language'] )
            return response
    
    return redirect('/')
    
def rootDir():
    thisfile = dirname(abspath(__file__))
    return normpath(join(thisfile, '../')).replace('\\', '/') 

def getLanguageIndex(language):
    result = 0
    
    try:
        result = LanguageMap[language]
    except:
        pass
    
    return result

def getLanguageIndexByRequest(request):
    result = 0
    
    if request.COOKIES.has_key( 'language' ):
        try:
            result = LanguageMap[request.COOKIES['language']]
        except:
            pass
    else:
        request.COOKIES['language'] = 'rus'
    
    return result

def getLanguageByRequest(request):
    result = 'rus'
    
    if request.COOKIES.has_key( 'language' ):
        result = request.COOKIES['language']
    
    return result

def getPageDictionary(request, pagename):
    result = {}
    langIndex = getLanguageIndexByRequest(request)
    
    pageDict = Dictionary[pagename]
    
    for key in pageDict.iterkeys():
        result[key] = pageDict[key][langIndex]
        
    for key in TabDictionary.iterkeys():
        result[key] = TabDictionary[key][langIndex]
    
    for key in CommonDictioanry.iterkeys():
        result[key] = CommonDictioanry[key][langIndex]
    
        
    return result

def getPageString(page, stringId, language):
    result = ''
    
    try:
        result = Dictionary[page][stringId][getLanguageIndex(language)]
    except:
        pass
    
    return result

def getErrorList2(errors, pagename, language):
    errList = '<ul>'

    try:
        rootEl = ET.fromstring(errors)
    
        pageDict = Dictionary[pagename]
        langIndex = LanguageMap[language]
    
        for elem in rootEl.findall('./li'): 
            error = ''
            errorName = elem.text + 'Error'
            for key in pageDict.iterkeys():
                if errorName == key:
                    error = pageDict[key][langIndex]
                    break
                        
            if error:        
                errList = errList + '<li>' + error + '</li>'
            else:
                errList = errList + '<li>' + elem.text + '</li>'
    except:
        errList = errList + "Unexpected error %s" % sys.exc_info()[0]
        
    errList = errList + '</ul>'
    
    return errList #errList.encode('utf-8')

def getErrorList(errors):
    errList = '<ul>'

    rootEl = ET.fromstring(errors)
    
    for elem in rootEl.findall('.//li/ul/li'):
        errList = errList + '<li>' + elem.text + '</li>'
        
    errList = errList + '</ul>'
    
    return errList.encode('utf-8')


def get_hwid(request):
    import commands
    if not isLoggedIn(request):
        return redirect('/login/')
    
    response = commands.getoutput('/usr/local/bin/vcount/hardwareid')
    
    return HttpResponse(response)
    