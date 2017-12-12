from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^edit_profile/$', handle_edit_profile, name='edit_profile'),
    # url(r'^movie/detail/(?P<id>.*)/$', movie_detail, name='movie_detail'),

    # index dan dashboard
    url(r'^page_profile/$', index, name='page_profile'),
    url(r'^$', index, name='index'),
]
