from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from trainingPortal.models import Profile,Chapter,Page,Mode
from trainingPortal.forms import LearningTypeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from quiz.models import Progress

LEARNING_TYPES = {'1':'Activist', '2':'Reflector', '3':'Theorist', '4':'Pragmatist' }
def getMode():
	testing = Mode.objects.get(name = 'testing')
	return testing.enable
def index(request):
	context_dict = {}
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		context_dict['testing'] = getMode()
	return render(request, 'trainingPortal/index.html', context_dict)
def statistics(request):
	context_dict = {}
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		users = User.objects.order_by('username')
		all = 0.0
		progressusers=0
		allusers=0
		activists=0
		reflectors=0
		theorists=0
		pragmatists=0
		none=0
		for user in users:
			try:
				progress = Progress.objects.get(user=user)
				type=user.profile.learningType
				if type=='1':
					activists = activists + 1
				if type=='2':
					reflectors = reflectors + 1
				if type=='3':
					theorists = theorists + 1
				if type=='4':
					pragmatists = pragmatists + 1
				if type=='0':
					none = none + 1
				print "TYPE"
				print type
				str = progress.score
				val = str.split(',')
				size = len(val)-1
				times = size / 3
				t=0
				a=0
				scores =[[{}] for t in range(0,times) ]
				t=0
				sum = 0.0
				while t<size-1:
					percentage =  (float(val[t+1])/float(val[t+2]))*100.0
					sum = sum + percentage
					score = [{'chapter': val[t], 'correct': val[t+1], 'all':val[t+2],'percentage':percentage}]
					scores[a]=score
					t=t+3
					a=a+1
					if a == times:
						break
				personal = True
				all = all + sum / times
				progressusers=progressusers+1
				allusers=allusers+1
			except Progress.DoesNotExist:
				pro = False
				allusers=allusers+1
				type=user.profile.learningType
				if type=='1':
					activists = activists + 1
				if type=='2':
					reflectors = reflectors + 1
				if type=='3':
					theorists = theorists + 1
				if type=='4':
					pragmatists = pragmatists + 1
				if type=='0':
					none = none + 1
		context_dict['all'] = all / progressusers
		context_dict['percentageall'] = (float(all / progressusers)/float(100))*100.0
		context_dict['progressusers'] = progressusers
		if progressusers!=0:
			context_dict['progressavailable'] = True
			context_dict['percentage']=(float(activists)/float(allusers))*100.0
		else:
			context_dict['progressavailable'] = False
			context_dict['percentage']=100.0
		context_dict['allusers'] = allusers
		context_dict['activists'] = activists
		if activists!=0:
			context_dict['activistsavailable'] = True
			context_dict['activistspercentage']=(float(activists)/float(allusers))*100.0
		else:
			context_dict['activistsavailable'] = False
			context_dict['activistspercentage']=100.0
		context_dict['reflectors'] = reflectors
		if reflectors!=0:
			context_dict['reflectorsavailable'] = True
			context_dict['reflectorspercentage']=(float(reflectors)/float(allusers))*100.0
		else:
			context_dict['reflectorsavailable'] = False
			context_dict['reflectorspercentage']=100.0
		context_dict['theorists'] = theorists
		if theorists!=0:
			context_dict['theoristsavailable'] = True
			context_dict['theoristspercentage']=(float(theorists)/float(allusers))*100.0
		else:
			context_dict['theoristsavailable'] = False
			context_dict['theoristspercentage']=100.0
		context_dict['pragmatists'] = pragmatists
		if pragmatists!=0:
			context_dict['pragmatistsavailable'] = True
			context_dict['pragmatistspercentage']=(float(pragmatists)/float(allusers))*100.0
		else:
			context_dict['pragmatistsavailable'] = False
			context_dict['pragmatistspercentage']=100.0
		context_dict['none'] = none
		if none!=0:
			context_dict['noneavailable'] = True
			context_dict['nonepercentage']=(float(none)/float(allusers))*100.0
		else:
			context_dict['noneavailable'] = False
			context_dict['nonepercentage']=100.0
	return render(request, 'trainingPortal/statistics.html', context_dict)
def chapters(request):
	context_dict = {}
	if request.user.is_authenticated():
		chapters = Chapter.objects.order_by('number')
		number = Chapter.objects.order_by('number').count()
		context_dict = {'chapters': chapters}
		context_dict['number'] = number
		for chapter in chapters:
			chapter.url = chapter.title.replace(':','_111_').replace('=','_121_').replace('&', '_131_').replace(' ', '_')
		context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/chapters.html', context_dict)
def about(request):
	context_dict = {}
	return render(request, 'trainingPortal/about.html', context_dict)
def learningType(request):
	context_dict = {}
	if request.user.is_authenticated():
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
	exists = True
	if request.user.is_authenticated():
		chapter_tl = chapter_title.replace('_111_',':').replace('_121_','=').replace('_131_','&').replace('_', ' ')
		try:
		    chapt = Chapter.objects.get(title = chapter_tl)
		    pages = Page.objects.filter(chapter = chapt)
		    pages = pages.order_by('number')
		    context_dict['chapter'] = chapter_title
		    context_dict['title'] = chapter_tl
		    context_dict['pages'] = pages
		    for page in pages:
		        page.url = page.title.replace(':','_111_').replace('=','_121_').replace('&', '_131_').replace(' ', '_')
		except Chapter.DoesNotExist:
		    exists = False
		chapters = Chapter.objects.order_by('title')
		for chapter in chapters:
			chapter.url = chapter.title.replace(':','_111_').replace('=','_121_').replace('&', '_131_').replace(' ', '_')
		context_dict ['chapters'] = chapters
		context_dict['exists'] = exists
		context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/chapter.html', context_dict)
def page(request,chapter_title,page_title):
    context_dict = {}
    exists = True
    if request.user.is_authenticated():
		title= page_title.replace('_111_',':').replace('_121_','=').replace('_131_','&').replace('_', ' ')
		chapter_tl = chapter_title.replace('_111_',':').replace('_121_','=').replace('_131_','&').replace('_', ' ')
		try:
		    chapt = Chapter.objects.get(title = chapter_tl)
		    page = Page.objects.get(chapter = chapt, title = title)
		    mode = page.learningStyleMode
		    user = request.user
		    profile = user.profile
		    testing = getMode()
		    context_dict['testing'] = testing
		    if testing:
		        if profile.testingType == '0':
		            context_dict ['entry'] = page.entry_default
		        else:
		            if mode:
		                ENTRY_TYPES = {'1':page.entry_Activist_Type, '2':page.entry_Reflector_Type, '3':page.entry_Theorist_Type, '4':page.entry_Pragmatist_Type }
		                context_dict['entry'] = ENTRY_TYPES.get(profile.learningType)
		            else:
		                context_dict ['entry'] = page.entry_default
		    else:
		        if mode:
		            ENTRY_TYPES = {'1':page.entry_Activist_Type, '2':page.entry_Reflector_Type, '3':page.entry_Theorist_Type, '4':page.entry_Pragmatist_Type }
		            context_dict['entry'] = ENTRY_TYPES.get(profile.learningType)
		        else:
		            context_dict ['entry'] = page.entry_default
		    context_dict ['chapter_url'] = chapter_title
		    context_dict ['chapter'] = chapter_tl
		    context_dict ['title'] = title
		    context_dict ['page'] = page
		    pages = Page.objects.filter(chapter = chapt)
		    context_dict ['pages'] = pages
		    for page in pages:
		        page.url = page.title.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_')
		except Page.DoesNotExist:
		    exists= False
		except Chapter.DoesNotExist:
		    exists= False
		chapters = Chapter.objects.order_by('title')
		for chapter in chapters:
		    chapter.url = chapter.title.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_')
		context_dict ['chapters'] = chapters
		context_dict['exists'] = exists
		context_dict['set_learningType'] = completedLearningStyle(request.user)
    return render(request, 'trainingPortal/page.html', context_dict)

def profile(request,username):
	context_dict = {"username" : username}
	exists = True
	personal = False
	pro = True
	testing = getMode()
	context_dict['testing'] = testing
	if request.user.is_authenticated():
		if request.user.username == username:
		    try:
		        progress = Progress.objects.get(user=request.user)
		        str = progress.score
		        val = str.split(',')
		        size = len(val)-1
		        times = size / 3
		        t=0
		        a=0
		        scores =[[{}] for t in range(0,times) ]
		        t=0
		        sum = 0.0
		        while t<size-1:
		            percentage =  (float(val[t+1])/float(val[t+2]))*100.0
		            sum = sum + percentage
		            score = [{'chapter': val[t], 'correct': val[t+1], 'all':val[t+2],'percentage':percentage}]
		            scores[a]=score
		            t=t+3
		            a=a+1
		            if a == times:
		                break
		        personal = True
		        if sum!=0.0:
		             context_dict['average'] = sum / times
		        else:
		             context_dict['average'] = sum

		        context_dict['scores'] = scores

		    except Progress.DoesNotExist:
		        pro = False
		context_dict['hasprogress'] = pro
		try:
			usr = User.objects.get(username = username)
			if personal:
				context_dict['user'] = usr
			else :
				context_dict['usr'] = usr
			if testing:
				if usr.profile.testingType =='0':
					context_dict['type'] = True
				else:
					context_dict['type'] = False
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
		context_dict['personal'] = personal
		context_dict['set_learningType'] = completedLearningStyle(request.user)
	return render(request, 'trainingPortal/profile.html', context_dict)
def completedLearningStyle(user):
	if (user.profile.learningType == '0'):
		return False
	else :
		return True