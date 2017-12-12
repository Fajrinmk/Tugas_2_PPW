from django.shortcuts import render
from .models import Mahasiswa

# Create your views here.
response = {}
def index(request):
	mahasiswa_list = Mahasiswa.objects.all().values()
	html = 'cari_mahasiswa/tables/mahasiswa.html'
	response = {"mahasiswa_list" : mahasiswa_list}
	return render(request, html, response)