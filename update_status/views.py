from __future__ import unicode_literals
import json
from .forms import Status_Form
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import pytz
from datetime import *
from .models import Pengguna, Status, Comment
from halaman_riwayat import views 
from django.core import serializers
from page_profile.views import index
from page_profile.models import User

response = {}
def index(request):
	if 'user_login' in request.session:
		return HttpResponseRedirect(reverse('update-status:dashboard'))
	else:

		response['author'] = get_data_user(request, 'user_login')
		npm = request.session['kode_identitas']
		user = (User.objects.filter(kode_identitas=npm).values('firstName', 'lastName','imageUrl','email','profileUrl','kode_identitas'))
		if(user):
			response['user'] = user[0]
		html = 'page_status/page_status.html'
		return render(request, html, response)
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
		response['Status_form'] = Status_Form
		kode_identitas = get_data_user(request,'kode_identitas')
		pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
		response['status'] = pengguna.status_set.all()
		# print(response['status'])
		stat = Status.objects.all().order_by('-id')
		if (len(stat) > 0):
			message = stat[0]
			newMessage = message.status
			time = message.created_date
		else:
			newMessage = "You have not posted yet" 
			time = date(datetime.now().year,datetime.now().month,datetime.now().day)
		response['latestMessage'] = newMessage
		response['jumlah_status'] = pengguna.status_set.count()
		response['daftar_riwayat'] = views.get_daftar_riwayat()
		html = 'update_status/dashboard.html'
		return render(request, html, response)

def add_status(request):
	kode_identitas = get_data_user(request,'kode_identitas')
	pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
	form = Status_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['status'] = request.POST['status']
		status = Status(status=response['status'], pengguna=pengguna)
		status.save()
	return HttpResponseRedirect(reverse('update-status:dashboard'))

def delete_status(request, id):
	kode_identitas = get_data_user(request,'kode_identitas')
	pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
	status = pengguna.status_set.filter(pk=id)
	status.delete()
	return HttpResponseRedirect(reverse('update-status:dashboard'))


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
