from django.conf.urls import url
from .views import *

urlpatterns = [
    # index dan dashboard
    url(r'^$', index, name='index'),
]