from django.db import models
import socket, os, sys, ast
from vCountDjGui.auxilary import rootDir 
import datetime
from settings.models import ServiceSettings
from xml.etree import ElementTree as et
import logging

logger = logging.getLogger(__name__)

# Create your models here.

def getHNFormInitials():
    initials = {}
    initials['hostname'] = socket.gethostname().decode('cp1251')
    return initials

def setHostName(cd):
    result = True
    reason = ''
    try:
        hostname = cd['hostname']
        oldhostname = socket.gethostname().decode('cp1251')
        if hostname != oldhostname:
            with open(os.path.join(rootDir(), 'vCount/hostname'), 'w') as fd:
                fd.write(hostname)
        else:
            result = False
            reason = 'Hostname is the same!'
    except:
        result = False
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
    return result, reason

def getDateTimeFormInitials():
    initials = {}
    now = datetime.datetime.now()
    initials['datetimefield'] = now.strftime("%Y-%m-%d %H:%M")
    return initials

def setDateTime(cd):
    result = True
    reason = ''
    try:
        dtstring = cd['datetimefield']
        with open(os.path.join(rootDir(), 'vCount/datetime'), 'w') as fd:
            fd.write(dtstring)
    except:
        result = False
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
    return result, reason

def setLogsEmail(cd):
    result = True
    reason = ''
    try:
        email = cd['emailto']
        with open(os.path.join(rootDir(), 'vCount/logs'), 'w') as fd:
            fd.write(email)
    except:
        result = False
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
    return result, reason

''' Resend date handlers '''
def resendateFormInitials():
    initials = {}
    now = datetime.datetime.now()
    initials['resenddate'] = now.strftime("%Y-%m-%d") + ' 12:00'
    return initials

def setResendData(cd):
    result = True
    reason = ''
    try:
        resendfrom = 'All'
        resendtype = cd['resendtype']
        
        if resendtype == '2':
            resendfrom = cd['resenddate']
            
        with open(os.path.join(rootDir(), 'vCount/resend.flag'), 'w') as fd:
            fd.write(resendfrom)
    except:
        result = False
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
    return result, reason

''' Notifications handlers '''
def notificationsInitials():
    settings = ServiceSettings()
    initials = {}
    initials['notify'] = ast.literal_eval(settings.content.find('Logging/To__Log').text)
    initials['notificationemail'] = settings.content.find('Logging/UseMail').text
    
    return initials

def setNotificationsSettings(cd):
    result = True
    reason = ''
    
    try:
        settings = ServiceSettings()
        
        tolog = cd['notify']
        settings.content.find('Logging/To__Log').text = str(tolog)
        
        if tolog:
            settings.content.find('Logging/UseMail').text = str(cd['notificationemail'])
        
        settings.writeSettings();
    except:
        result = False
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
    return result, reason

def getIpSettings():
    ipSettingsPath = os.path.join(rootDir(),'vCount/ipconfig.xml')
    
    tree = et.ElementTree()
    try:
        tree = et.parse(ipSettingsPath)
    except:
        logger.error('ipconfig error!')
    
    return tree

def setIpSettings(settings):
    #ipSettingsPath = os.path.join(rootDir(),'vCount/ipconfig.xml')
    #settings.write(ipSettingsPath)
    with open(os.path.join(rootDir(),'vCount/ipconfig.xml'), 'w') as fd:
        fd.write(settings)
    
    with open(os.path.join(rootDir(),'vCount/ipconfig.flag'), 'w') as fd:
        fd.write('flag')
        
def getWifiEssids():
    essidList = []
    essidsPath = os.path.join(rootDir(),'vCount/scan.dat')
    
    try:
        with open(essidsPath, 'r') as fd:
            try:
                essidList = [(line.rstrip('\n'), line.rstrip('\n')) for line in fd]
                essidList = tuple(essidList)
            except:
                logger.error('scan.dat error 1!')    
    except:
        logger.error('scan.dat error 2!')
        
    return essidList

def getIpConfigInitials():
    initials = {}
    
    try:
        ipsettings = getIpSettings()
    
        initials['networktype'] = ipsettings.find('NetworkType').text
        initials['wifiessid'] = ipsettings.find('WifiESSIDName').text
        initials['wifipassword'] = ipsettings.find('WifiPassword').text
        initials['iptype'] = ipsettings.find('IpConfigType').text
        initials['ipaddress'] = ipsettings.find('IpAddress').text
        initials['ipmask'] = ipsettings.find('Mask').text
        initials['gateway'] = ipsettings.find('Gateway').text
        initials['dnsserver'] = ipsettings.find('DnsServer').text
    except:
        logger.error('getIpConfigInitials error!')
    
    return initials

def setNetworkSettings(cd):
    result = True
    reason = ''
    
    try:
        '''ipsettings = getIpSettings()
    
        ipsettings.find('NetworkType').text = cd['networktype']
        ipsettings.find('WifiESSIDName').text = cd['wifiessid']
        ipsettings.find('WifiPassword').text = cd['wifipassword']
    
        ipsettings.find('IpConfigType').text = cd['iptype']
        ipsettings.find('IpAddress').text = cd['ipaddress']
        ipsettings.find('Mask').text = cd['ipmask']
        ipsettings.find('Gateway').text = cd['gateway']
        ipsettings.find('DnsServer').text = cd['dnsserver']'''
        
        ipsettings = et.Element('NetworkConfiguration')
        
        networkType = et.SubElement(ipsettings, 'NetworkType')
        networkType.text = cd['networktype']
        
        wifiESSIDName = et.SubElement(ipsettings, 'WifiESSIDName')
        wifiESSIDName.text = cd['wifiessid']
        
        wifiPassword = et.SubElement(ipsettings, 'WifiPassword')
        wifiPassword.text = cd['wifipassword']
        
        IpConfigType = et.SubElement(ipsettings, 'IpConfigType')
        IpConfigType.text = cd['iptype']
        
        IpAddress = et.SubElement(ipsettings, 'IpAddress')
        IpAddress.text = cd['ipaddress']
        
        Mask = et.SubElement(ipsettings, 'Mask')
        Mask.text = cd['ipmask']
        
        Gateway = et.SubElement(ipsettings, 'Gateway')
        Gateway.text = cd['gateway']
        
        DnsServer = et.SubElement(ipsettings, 'DnsServer')
        DnsServer.text = cd['dnsserver']
        
        xml = et.tostring(ipsettings)
        setIpSettings(xml)
    except:
        result = False
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
    
    return result, reason
    
    