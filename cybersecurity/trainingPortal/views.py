from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from trainingPortal.models import Profile,Chapter,Page
from trainingPortal.forms import LearningTypeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


LEARNING_TYPES = {'1':'Activist', '2':'Reflector', '3':'Theorist', '4':'Pragmatist' }

def index(request):
	context_dict = {}
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/index.html', context_dict)
def chapters(request):
	chapters = Chapter.objects.order_by('title')
	context_dict = {'chapters': chapters}
	for chapter in chapters:
		chapter.url = chapter.title.replace(' ', '_')
	context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/chapters.html', context_dict)
def about(request):
	context_dict = {}
	return render(request, 'trainingPortal/about.html', context_dict)
def learningType(request):
	context_dict = {}
	context_dict['set_learningType'] = completedLearningStyle(request.user)
	if request.method == 'POST':
		form = 	LearningTypeForm(request.POST)
		user = request.user
		profile = user.profile
		print profile
		if form.is_valid():
			form = 	LearningTypeForm(request.POST, instance=profile)
			form.save()
			return index(request)
		else:
			print form.errors
	else:
		form = 	LearningTypeForm()
	context_dict['form'] = form
	return render(request, 'trainingPortal/learningtype.html', context_dict)
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
	chapters = Chapter.objects.order_by('title')
	for chapter in chapters:
		chapter.url = chapter.title.replace(' ', '_')
	context_dict ['chapters'] = chapters
	context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/chapter.html', context_dict)
def page(request,chapter_title,page_title):
	context_dict = {}
	title= page_title.replace('_',' ')
	chapter_tl = chapter_title.replace('_', ' ')
	chapt = Chapter.objects.get(title = chapter_tl)
	page = Page.objects.get(chapter = chapt, title = title)
	mode = page.learningStyleMode
	pages = Page.objects.filter(chapter = chapt)
	user = request.user
	profile = user.profile
	if mode:
		ENTRY_TYPES = {'1':page.entry_Activist_Type, '2':page.entry_Reflector_Type, '3':page.entry_Theorist_Type, '4':page.entry_Pragmatist_Type }
		context_dict['entry'] = ENTRY_TYPES.get(profile.learningType)
	else:
		context_dict ['entry'] = page.entry_default
	context_dict ['chapter_url'] = chapter_title
	context_dict ['chapter'] = chapter_tl
	context_dict ['pages'] = pages
	context_dict ['title'] = title
	for page in pages:
		page.url = page.title.replace(' ', '_')
		print page.url
	chapters = Chapter.objects.order_by('title')
	for chapter in chapters:
		chapter.url = chapter.title.replace(' ', '_')
	context_dict ['chapters'] = chapters
	context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/page.html', context_dict)
	
def profile(request,username):
	context_dict = {"username" : username}
	exists = True
	try:
		usr = User.objects.get(username = username)
		context_dict['user'] = usr
		try:
			profile = Profile.objects.get(user = usr)
			context_dict['age'] = profile.age
			context_dict['learningType'] = LEARNING_TYPES.get(profile.learningType)
			#learning style
			
		except Profile.DoesNotExist:
			exists = False
	except User.DoesNotExist:
		exists = False
	context_dict['exists'] = exists
	context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/profile.html', context_dict)

def completedLearningStyle(user):
	if (user.profile.learningType == '0'):
		return False 	
	else :
		return True