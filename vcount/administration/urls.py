'''
Created on 08.08.2013

@author: alexander.kozlov@itseez.com
'''
from django.conf.urls import patterns, url
from administration import views

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
    url(r'^changehostname/$', views.changeHostName),
    url(r'^changedatetime/$', views.changeDateTime),
    url(r'^sendlogs/$', views.sendLogs),
    url(r'^resendata/$', views.resendData),
    url(r'^setnotifications/$', views.setNotifications),
    url(r'^setnetwork/$', views.setNetwork),
)