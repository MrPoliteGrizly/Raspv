import os
import sys
from os.path import join, abspath, normpath, dirname

ProjectDir = dirname(abspath(__file__))

def tpl_dir(src):
    return normpath(join(ProjectDir, src)).replace('\\', '/') 

sys.path.append(tpl_dir('../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'vCountDjGui.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()