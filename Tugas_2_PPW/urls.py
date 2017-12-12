"""Tugas_2_PPW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import update_status.urls as update_status
import halaman_profile.urls as page_profile
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^update_status/', include(update_status,namespace='update-status')),

    url(r'^page_profile/', include(page_profile,namespace='page-profile')),
    url(r'^$', RedirectView.as_view(url='page_profile/',permanent=True),name='$'),

    url(r'^halaman_riwayat/', include(update_status,namespace='halaman-riwayat')),
    url(r'^halaman_profile/', include(update_status,namespace='halaman-profile')),
    url(r'^$', RedirectView.as_view(url='update_status/',permanent=True),name='$'),

]
