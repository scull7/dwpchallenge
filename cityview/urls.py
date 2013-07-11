from django.conf.urls import patterns, include, url
from cityview import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^county/(?P<county_id>\d+)/$', views.IndexView.as_view(), name='county'),
)