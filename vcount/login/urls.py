'''
Created on 22.07.2013

@author: User
'''

from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vCountDjGui.views.home', name='home'),
    # url(r'^vCountDjGui/', include('vCountDjGui.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #TemplateView.as_view(template_name= 'settings_detail.html')
    url(r'^$', views.index),
)