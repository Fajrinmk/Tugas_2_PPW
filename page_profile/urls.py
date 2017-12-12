from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^edit_profile/$', edit_profile, name='edit_profile'),
    url(r'^save_to_database/$', save_to_database, name='save_to_database'),
    url(r'^$', index, name='index'),
]
