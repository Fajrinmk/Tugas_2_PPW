from django.conf.urls import url
from .views import *

from .custom_auth import auth_login, auth_logout

urlpatterns = [
    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

    # index dan dashboard
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
]