from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from vCountDjGui import settings
from vCountDjGui import auxilary

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vCountDjGui.views.home', name='home'),
    # url(r'^vCountDjGui/', include('vCountDjGui.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', include('settings.urls')),
    (r'^settings/', include('settings.urls')),
    (r'^channels/$', include('channels.urls')),
    (r'^administration/', include('administration.urls')),
    (r'^update/', include('update.urls')),
    (r'^password/', include('password.urls')),
    (r'^changelanguage/$', auxilary.changeLanguage),
    (r'^exit/$', auxilary.closeSession),
    (r'^hardwareid/$', auxilary.get_hwid),
    (r'^login/$', include('login.urls')), 
    #TemplateView.as_view(template= 'settings/settings_detail.html')
    #url(r'^settings/$', 'settings.views.SettingsView', TemplateView.as_view(template_name= 'settings/settings_detail.html')),
)


if settings.DEBUG:
    '''urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),)'''
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
