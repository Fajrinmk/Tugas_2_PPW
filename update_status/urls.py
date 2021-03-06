from django.conf.urls import url
from .views import *
from page_profile.views import edit_profile
#import view profile


from .custom_auth import auth_login, auth_logout

urlpatterns = [
    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

    # index dan dashboard
    url(r'^$', index, name='index'),
    url(r'^dashboard/edit_profile', edit_profile, name='edit_profile'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^add_status/', add_status, name='add_status'),
    url(r'^delete/(?P<id>\d+)/', delete_status, name='delete'),
]