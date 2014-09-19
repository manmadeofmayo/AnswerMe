from django.conf.urls.defaults import url, patterns
from django.contrib import admin
from django.views.generic.simple import redirect_to
import authentication.views

__author__ = 'emcee'

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^confirm/(?P<activation_key>\w+)/', authentication.views.confirm),
    url(r'^register/$', authentication.views.register, name='register'),
    url(r'^login/$', authentication.views.login, name="login"),
    url(r'^logout/$', authentication.views.logout, name="logout")
)
