from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

# Create your views here.
response = {}
RIWAYAT_API = 'https://private-e52a5-ppw2017.apiary-mock.com/riwayat'

def index(request):
	response['daftar_riwayat'] = get_daftar_riwayat()
	# response['rahasia'] =
	html = 'halaman_riwayat/riwayat.html'
	return render(request, html, response)

def get_daftar_riwayat():
	daftar_riwayat = requests.get(RIWAYAT_API)
	return daftar_riwayat.json()
