from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<username>.*)/$', index, name='index'),
    url(r'^add-expertise/(?P<expertise>.*)/(?P<level>.*)/$', addExpertise, name='addExpertise'),
    url(r'^edit-profile', edit_profile, name='edit_profile')
]
