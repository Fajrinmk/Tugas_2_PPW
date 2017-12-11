from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^halaman_riwayat$', get_data_mhs , name='get_data_mhs'),
]