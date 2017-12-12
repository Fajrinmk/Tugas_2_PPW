from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

# Create your views here.
response = {}
RIWAYAT_API = 'https://private-e52a5-ppw2017.apiary-mock.com/riwayat'

def index(request):
	response['daftar_riwayat'] = get_riwayat()
	html = 'halaman_riwayat/riwayat.html'
	return render(request, html, response)

def get_riwayat():
	riwayat = requests.get(RIWAYAT_API)
	return riwayat.json()
