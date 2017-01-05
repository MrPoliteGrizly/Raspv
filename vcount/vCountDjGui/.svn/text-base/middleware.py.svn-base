'''
Created on 13.08.2013

@author: alexander.kozlov@itseez.com
'''

from vCountDjGui import settings

class SessionExpiry(object):
    """ Set the session expiry according to settings """
    def process_request(self, request):
        if getattr(settings, 'SESSION_EXPIRY', None):
            request.session.set_expiry(settings.SESSION_EXPIRY)
        return None