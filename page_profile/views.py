from django.shortcuts import render
from datetime import datetime, date
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from .models import User

# Create your views here.

from django.shortcuts import render

response = {}

def index(request):
    # print ("#==> masuk index")
    if 'user_login' in request.session:
        response['login'] = True
        return HttpResponseRedirect(reverse('page_status:index'))
    else:
        response['login'] = False
        response['author'] = get_data_user(request, 'user_login')
        html = 'update_status/login.html'
        return render(request, html, response)

def profile(request):
    if not 'user_login' in request.session.keys():
        return HttpResponseRedirect(reverse('mahasiswa:index'))
    else:

        html = 'profile/profile.html'
        return render(request, html, response)

def edit_profile(request):
    html = 'page_profile/edit_profile.html'
    response['kode_identitas'] = request.session['kode_identitas']
    return render(request, html, response)

def get_data_user(request, tipe):
    data = None
    if tipe == "user_login" and 'user_login' in request.session:
        data = request.session['user_login']
    elif tipe == "kode_identitas" and 'kode_identitas' in request.session:
        data = request.session['kode_identitas']

    return data

def get_data_session(request):
    if get_data_user(request, 'user_login'):
        response['author'] = get_data_user(request, 'user_login')

def set_data_for_session(request):
    response['author'] = get_data_user(request, 'user_login')
    response['kode_identitas'] = request.session['kode_identitas']

@csrf_exempt
def save_to_database(request):
    if(request.method == 'POST'):
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        imageUrl = request.POST['imageUrl']
        email = request.POST['email']
        profileUrl = request.POST['profileUrl']
        kode_identitas = request.session['kode_identitas']
        exist = User.objects.filter(kode_identitas=kode_identitas).exists()
        if(not exist):
            user = User(firstName=firstName, lastName=lastName, imageUrl=imageUrl, email=email, profileUrl=profileUrl, kode_identitas=kode_identitas)
            user.save()
        return JsonResponse({'save':'ok'})
#
# def show_form_edit_profile(request):
#      html = "page_profile/edit_profile.html"
#      profile = DataProfile.objects.first()
#      response['profile'] = profile
#      return render(request, html, response)
