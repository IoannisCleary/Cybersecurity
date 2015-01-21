from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from trainingPortal.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	context_dict = {}
	return render(request, 'trainingPortal/index.html', context_dict)
def about(request):
	context_dict = {}
	return render(request, 'trainingPortal/about.html', context_dict)
def chapter(request,chapter_title):
	context_dict = {}
	return render(request, 'trainingPortal/chapter.html', context_dict)
def page(request,chapter_title,page_title):
	context_dict = {}
	return render(request, 'trainingPortal/page.html', context_dict)
def profile(request,username):
	context_dict = {"username" : username}
	usr = User.objects.get(username = username)
	profile =Profile.objects.get(user = usr)
	print usr.first_name
	context_dict['user'] = usr
	context_dict['profile'] = profile
	return render(request, 'trainingPortal/profile.html', context_dict)