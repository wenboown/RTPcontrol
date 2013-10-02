from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from Tcontrol import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.main_panel, name='main_panel'),
    #url(r'^add/', views.add, name='add'),
    url(r'^run/', views.run, name='run'),
    url(r'^standby/', views.standby, name='standby'),
    url(r'^operate/', views.operate, name='operate'),
    # url(r'^$', 'RTP.views.home', name='home'),
    # url(r'^RTP/', include('RTP.foo.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()