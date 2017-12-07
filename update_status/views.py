# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Pengguna, myStatus, myComment

response = {}
def index(request):
    # print ("#==> masuk index")
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('update-status:dashboard'))
    else:
        response['author'] = get_data_user(request, 'user_login')
        html = 'update_status/login.html'
        return render(request, html, response)


def dashboard(request):
	if 'user_login' not in request.session:
		response['author'] = get_data_user(request, "user_login")
		html = 'update_status/login.html'
		return render(request, html, response)
	else:
		set_data_for_session(request)
		kode_identitas = get_data_user(request, 'kode_identitas')
		try:
			pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
		except Exception as e:
			pengguna = create_new_user(request)

		html = 'update_status/dashboard.html'
		return render(request, html, response)

def get_data_user(request, tipe):
    data = None
    if tipe == "user_login" and 'user_login' in request.session:
        data = request.session['user_login']
    elif tipe == "kode_identitas" and 'kode_identitas' in request.session:
        data = request.session['kode_identitas']

    return data

def create_new_user(request):
    nama = get_data_user(request, 'user_login')
    kode_identitas = get_data_user(request, 'kode_identitas')

    pengguna = Pengguna()
    pengguna.kode_identitas = kode_identitas
    pengguna.nama = nama
    pengguna.save()

    return pengguna

### SESSION : GET and SET
def get_data_session(request):
    if get_data_user(request, 'user_login'):
        response['author'] = get_data_user(request, 'user_login')

def set_data_for_session(request):
    response['author'] = get_data_user(request, 'user_login')
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']