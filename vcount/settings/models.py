import os, sys, ast
from django.db import models
from settings.settingsparser import SettingsData
from xml.etree import ElementTree as et
from vCountDjGui.auxilary import rootDir

# Create your models here.

class ServiceSettings():
    settingsPath = os.path.join(rootDir(),'vCount/settings_decrypted.xml')
        
    def __init__(self):
        self.content = et.parse(self.settingsPath)
        
    def writeSettings(self):
        result = True
        reason = ''
        
        try:
            self.content.write(self.settingsPath)
            #self.content.write(self.settingsPath, "CP1251") 
            with open(os.path.join(rootDir(), 'vCount/flag'), 'w') as fd:
                fd.write('flag')
        except:
            result = False
            reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
            
        return result, reason

    def __unicode__(self):
        return self.content.find('ShopID').text 
    
    
def manualhoursConverter(settings, data):
    if not data:
        result = ''
        root =  settings.content.getroot()
        for child in root.findall('./' + settingsMatch['manualhours'][0] + '/ReportTime'):
            result = result + child.find('Hour').text + ':' + child.find('Minute').text + ','
    
        if result:
            result = result[:-1]
        
            return result
    else:
        data = data.replace(' ', '')
        timelist = settings.content.find(settingsMatch['manualhours'][0])
        
        for child in timelist.findall('ReportTime'):
            timelist.remove(child) 
        
        for timeval in data.split(','):
            hm = timeval.split(':')
            
            rte = et.SubElement(timelist, 'ReportTime')
            
            he = et.SubElement(rte, 'Hour')
            he.text = hm[0]
            
            me = et.SubElement(rte, 'Minute')
            me.text = hm[1]

settingsMatch = {
               'shopid' :   ['ShopID', 'text'],
               'workallday' : ['WorkAllDay', 'bool'],
               'worktimefrom' : ['WorkTimeFrom', 'text'],
               'worktimetill' : ['WorkTimeTill', 'text'],
               'intervalhours' : ['Reports/ReportTimes/IntervalHours', 'text'],
               'ismanualhours' : ['Reports/ReportTimes/ManualSetting', 'bool'],
               'manualhours' : ['Reports/ReportTimes/TimeList', manualhoursConverter],
               'is1C' : ['Reports/is1C', 'bool'],
               'sendbyemail' : ['Reports/Email/Enabled', 'bool'],
               'emailto' : ['Reports/Email/To', 'text'],
               'sendtoserver': ['Reports/Server/Enabled', 'bool'],
               'serveraddress' : ['Reports/Server/IP', 'text'],
               'serverport' : ['Reports/Server/Port', 'text'],
               'useshared': ['Reports/Shared/Enabled', 'bool'],
               'sharepath' : ['Reports/Shared/Folder', 'text'],
               'shareuser' : ['Reports/Shared/User', 'text'],
               'sharepassword' : ['Reports/Shared/Password', 'text'],
               'emailfrom' : ['Reports/Email/From', 'text'],
               'smtpserver' : ['Reports/Email/SMTPServer', 'text'],
               'smtpport' : ['Reports/Email/SMTPPort', 'text'],
               'attemptstosend' : ['Reports/Email/NumberOfAttempts', 'text'],
               'useauthentication' : ['Reports/Email/Authentication', 'bool'],
               'smtpuser' : ['Reports/Email/Username', 'text'],
               'smtppassword' : ['Reports/Email/Password', 'text'],
               'usessl' : ['Reports/Email/EnableSSL', 'bool'],
}

def checkShopName(cd, settings):
    oldname = settings.content.find(settingsMatch['shopid'][0]).text
    newname = cd['shopid']
    
    if oldname != newname:
        filename = os.path.join(rootDir(), 'vCount/changeShopName')
        with open(filename, 'w') as fd:
            fd.write(''.join((oldname, '*', newname)))

def setSettingsToXML(form, settings):   
    cd  = form.cleaned_data

    checkShopName(cd, settings)

    for a, v in settingsMatch.iteritems():
        if v[1] == 'text' or v[1] == 'bool':
            settings.content.find(v[0]).text = str(cd[a])
        else:
            v[1](settings, str(cd[a]))
    
    return settings.writeSettings()

def setSettingsToView(settings):
    initial = {}
    for a, v in settingsMatch.iteritems():
        if v[1] == 'text':
            initial[a] = settings.content.find(v[0]).text
        elif v[1] == 'bool':
            initial[a] =  ast.literal_eval(settings.content.find(v[0]).text)
        else:
            initial[a] = v[1](settings, '')
    return initial