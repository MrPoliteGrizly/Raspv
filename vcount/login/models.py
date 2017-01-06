# -*- coding: utf-8 -*-
import os, sys, hashlib
from django.db import models
from vCountDjGui.auxilary import rootDir
# Create your models here.



def verifyLogin(login, password):
    result = True
    reason = ''
    '''
    try:
        passwordfile = os.path.join(rootDir(),'vCount/password.dat')
        fd = open(passwordfile)
        line = fd.readline()
        fd.close()
        
        reallogin, realpswd = line.split()
        
        try:
            hashedpswd = hashlib.sha1(password).hexdigest()

            if (login, hashedpswd) == (reallogin, realpswd):
                result = True
            else:
                reason = 'loginError'
        except:
            reason = 'loginError'

    except:
        reason = 'Server error: %s\n %s\n %s' %  (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
     '''   
    return result, reason