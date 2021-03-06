from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout_then_login


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dwpchallenge.views.home', name='home'),
    # url(r'^dwpchallenge/', include('dwpchallenge.foo.urls')),

    url(r'', include('cityview.urls', namespace='cityview')),
    url(r'^login', login),
    url(r'^logout', logout_then_login),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
