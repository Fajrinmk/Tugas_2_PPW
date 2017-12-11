from django.shortcuts import render
from datetime import datetime, date
from .models import DataProfile
from django.http import HttpResponseRedirect
# from .forms import edit_profile_form

# Create your views here.

profile_name = 'Gigi Hadid' #TODO implement your name here
birth_date = date(1995,4,23) #TODO implement your birthday
birthdate = birth_date.strftime('%d %B %Y')
gender = 'Female' #TODO implement your gender
email = 'gigihadid@gmail.com' #TODO implement your email
desc_profile = "victoria's secret model lalala lilili yeyeye"
#TODO implement your expertise minimal 3
# expert = ["fashion model", "actress", "wawww"]
expert = "fashion model, actress, wawww"

response = {}
def index(request):
    if (DataProfile.objects.count()==0):
        Profile = DataProfile(name= profile_name, birthday = birthdate, gender = gender,expertise = expert, email = email, description = desc_profile, id = 1 )
        Profile.save()
    profile = DataProfile.objects.first()
    response = {'Name':profile.name, 'Birthday':profile.birthday,'Gender':profile.gender,'Expertise':profile.expertise.split(","),'Email':profile.email,'Description':profile.description}
    return render(request, 'halaman_profile.html', response)
    
    #try new feature
def handle_edit_profile(request):
    # form = edit_profile_form(request.POST or None)
    # if(request.method == 'POST'and form.is_valid()):
    DataProfile.objects.all().delete()
    response['name'] = request.POST['profile_name']
    response['birthday'] = request.POST['birthdate']
    response['gender'] = request.POST['gender']
    response['expertise'] = request.POST['expert']
    response['email'] = request.POST['email']
    response['description'] = request.POST['desc_profile']
    edit = DataProfile(name= response['name'], birthday = response['birthday'], gender = response['gender'],expertise = response['expertise'], email = response['email'], description = response['description'] )
    edit.save()
    return HttpResponseRedirect('/halaman_profile/')

def show_form_edit_profile(request):
     html = "halaman_profile/edit_profile.html"
     profile = DataProfile.objects.first()
     response['profile'] = profile
     return render(request, html, response)
