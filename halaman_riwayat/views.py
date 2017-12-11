from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from hal_riwayat.js import database_mahasiswa

# Create your views here.
#index 
#mengambil data di js ngambil,parameter npm

response = {}

def index(request):
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('halaman_riwayat : riwayat'))
    else:
        response['login'] = False
        html = 'lab_9/session/login.html'
        return render(request, html, response)

# def get_data_kelas(access_token, id):
#     parameters = {"access_token": access_token, "client_id": get_client_id()}
#     response = requests.get(API_MAHASISWA+id, params=parameters)
#     return response.json()
