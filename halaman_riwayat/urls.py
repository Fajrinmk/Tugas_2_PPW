from django.conf.urls import url
from .views import index, get_daftar_riwayat

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^get_daftar_riwayat/$', get_daftar_riwayat, name='get_daftar_riwayat'),
]