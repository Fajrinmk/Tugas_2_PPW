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
    url(r'^add_status/', add_status, name='add_status'),
    url(r'^delete/(?P<id>\d+)/', delete_status, name='delete'),
    url(r'^get-status-list/$', status_list_json, name='get-status-list')
]