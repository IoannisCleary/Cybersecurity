from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from trainingPortal.models import Profile,Chapter,Page
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	context_dict = {}
	return render(request, 'trainingPortal/index.html', context_dict)
def chapters(request):
	chapters = Chapter.objects.order_by('title')
	context_dict = {'chapters': chapters}
	for chapter in chapters:
		chapter.url = chapter.title.replace(' ', '_')
	return render(request, 'trainingPortal/chapters.html', context_dict)
def about(request):
	context_dict = {}
	return render(request, 'trainingPortal/about.html', context_dict)
def chapter(request,chapter_title):
	context_dict = {}
	chapter_tl = chapter_title.replace('_', ' ')
	chapt = Chapter.objects.get(title = chapter_tl)
	pages = Page.objects.filter(chapter = chapt)
	context_dict['chapter'] = chapter_title
	context_dict['title'] = chapter_tl
	context_dict['pages'] = pages
	for page in pages:
		page.url = page.title.replace(' ', '_')
		print page.url
	return render(request, 'trainingPortal/chapter.html', context_dict)
def page(request,chapter_title,page_title):
	context_dict = {}
	title= page_title.replace('_',' ')
	chapter_tl = chapter_title.replace('_', ' ')
	chapt = Chapter.objects.get(title = chapter_tl)
	page = Page.objects.get(chapter = chapt, title = title)
	pages = Page.objects.filter(chapter = chapt)
	context_dict ['entry'] = page.entry
	context_dict ['chapter'] = chapter_tl
	context_dict ['pages'] = pages
	context_dict ['title'] = title
	return render(request, 'trainingPortal/page.html', context_dict)
def profile(request,username):
	context_dict = {"username" : username}
	usr = User.objects.get(username = username)
	profile =Profile.objects.get(user = usr)
	print usr.first_name
	context_dict['user'] = usr
	context_dict['profile'] = profile
	return render(request, 'trainingPortal/profile.html', context_dict)