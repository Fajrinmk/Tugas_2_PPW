from django.shortcuts import render
from .models import User, Expertise

response = {}


# Create your views here.
def index(request, username):
    user_count = User.objects.filter(username=username)
    if user_count == 0:
        user = User.objects.create(username=username)
        user.save()
    else:
        user = user_count.first()

    response['username'] = user.username
    response['npm'] = user.npm
    response['profile_pic'] = user.profile_pic
    response['flag_nilai'] = user.flag_nilai
    response['name'] = user.name
    response['expertise'] = user.expertise.all()
    response['email'] = user.email
    response['linkedin_profile'] = user.linkedin_profile

    html = 'aboutme/aboutme.html'
    return render(request, html, response)


def edit_profile(request):
    edited_user = User.objects.first()

    if (request.method == 'POST'):
        edited_user.name = request.POST['name']
        edited_user.email = request.POST['email']
        edited_user.linkedin_profile = request.POST['linkedin_profile']


def addExpertise(request, expertise, level):
    user = User.objects.first()
    expertise = Expertise.objects.filter(expertise=expertise, level=level)

    if expertise == 0:
        e = Expertise.objects.create(expertise=expertise, level=level)
        e.save()
        user.expertise.add(e)
    else:
        user.expertise.add(expertise.first())
