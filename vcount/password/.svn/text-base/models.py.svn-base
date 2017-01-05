# -*- coding: utf-8 -*-
import os, sys, hashlib
from django.db import models
from vCountDjGui.auxilary import rootDir, getPageDictionary, getPageString

# Create your models here.
def setPassword(cd, lang):
    result = False
    reason = ''
    
    try:
        oldpwd = cd['oldpassword']
        newpwd = cd['newpassword']
        newrepeatedpwd = cd['newrepeatedpassword']
        
        passwordfile = os.path.join(rootDir(),'vCount/password.dat')
        fd = open(passwordfile)
        line = fd.readline()
        fd.close()
        
        _, realpswd = line.split()
        
        hashedpswd = hashlib.sha1(oldpwd).hexdigest()        
    
        if hashedpswd == realpswd:
            if newpwd == newrepeatedpwd:
                newhashedpswd = hashlib.sha1(newpwd).hexdigest()
                strtowrite = 'vcount %s' % newhashedpswd
                
                with open(passwordfile, 'w') as fd:
                    fd.write(strtowrite)
                
                result = True
            else:
                reason = getPageString('passwordForm', 'passwordNotEqual', lang)
        else:
            reason = getPageString('passwordForm', 'incorrectOldPassword', lang)

    except:
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        
    return result, reason