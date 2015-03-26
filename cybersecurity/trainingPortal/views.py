from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from trainingPortal.models import Profile,Chapter,Page,Mode,PageExercise,Exercise,Announcement,IndexElement
from trainingPortal.forms import LearningTypeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from quiz.models import Progress,Sitting,Quiz,Category

LEARNING_TYPES = {'1':'Activist', '2':'Reflector', '3':'Theorist', '4':'Pragmatist' }
def getMode():
	testing = Mode.objects.get(name = 'testing')
	return testing.enable
def index(request):
	context_dict = {}
	hasAnnouncement=False
	hasIndex=False
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		context_dict['testing'] = getMode()
		try:
		    announcements = Announcement.objects.all().order_by('-number')[:3]
		    hasAnnouncement=True
		    context_dict['announcements'] = announcements
		except Announcement.DoesNotExist:
		    hasAnnouncement=False
		try:
		    indexelements = IndexElement.objects.all()
		    hasIndex=True
		    context_dict['indexelements'] = indexelements
		except IndexElement.DoesNotExist:
		    hasIndex=False
		context_dict['hasIndex'] = hasIndex
		context_dict['hasAnnouncement'] = hasAnnouncement


	return render(request, 'trainingPortal/index.html', context_dict)

def help(request):
	context_dict = {}
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		context_dict['testing'] = getMode()
	return render(request, 'trainingPortal/help.html', context_dict)
def statistics(request):
	context_dict = {}
	testing = getMode()
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		users = User.objects.order_by('username')
		all = 0.0
		allT = 0.0
		progressusers=0
		progressusersT=0
		allusers=0
		activists=0
		reflectors=0
		theorists=0
		pragmatists=0
		none=0
		for user in users:
			print user.username
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
				ignore='Example' #category
				t=0
				while t<size-1:
				    if val[t].lower() == ignore.lower():
				        times = times - 1
				        break;
				    t=t+3


				t=0
				a=0
				scores =[[{}] for t in range(0,times) ]
				t=0

				sum = 0.0
				sumT=0.0
				valid=0
				validT=0
				while t<size-1:
				    print t;
				    if val[t].lower() != ignore.lower():
				        cat = Category.objects.get(category=val[t])
				        quizzes = Quiz.objects.filter(category=cat)
				        q=0
				        qsum=0.0
				        tsum=0.0
				        tq=0
				        for quiz in quizzes:
				            sitting = Sitting.objects.filter(user=user, quiz=quiz,testing=False).order_by('-end')[:1]
				            if sitting.count()>0:

				                percentage =  sitting[0].get_percent_correct
				                qsum=qsum+percentage
				                q=q+1
				                valid=valid+1
				        for quiz in quizzes:
				            sitting = Sitting.objects.filter(user=user, quiz=quiz,testing=True).order_by('-end')[:1]
				            if sitting.count()>0:
				                percentage =  sitting[0].get_percent_correct
				                tsum=tsum+percentage
				                tq=tq+1
				                validT=validT+1
				        # qz = Quiz.objects.get(title=val[t])
				        percent = 0.0
				        percentQ = 0.0
				        if q>0:
				            percent = (float(qsum / q)/float(100))*100.0
				        if tq>0:
				            percentQ = (float(tsum / tq)/float(100))*100.0
				        sum = sum + percent
				        sumT = sumT + percentQ
				        score = [{'chapter': val[t], 'correct': val[t+1], 'all':val[t+2],'percentage':percent}]
				        scores[a]=score

				        a=a+1
				    t=t+3
				    if a == times:
						break
				personal = True
				if sum!=0.0:
				    all = all + sum / times
				    if sumT>0.0:
				        allT = allT + sumT / times
				        progressusersT=progressusersT+1
				    progressusers=progressusers+1
				elif valid>0:
				    if sumT>0.0:
				        print sumT
				        allT = allT + sumT / times
				        progressusersT=progressusersT+1
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
		if all!=0:
		    context_dict['hasall'] = True
		    context_dict['all'] = all / progressusers
		    context_dict['percentageall'] = (float(all / progressusers)/float(100))*100.0
		else:
		    context_dict['all'] = 0
		    context_dict['hasall'] = False
		    context_dict['percentageall'] = 100.0
		if allT!=0:
		    context_dict['hasTesting'] = True
		    context_dict['allT'] = allT / progressusersT
		    context_dict['percentageallT'] = (float(allT / progressusersT)/float(100))*100.0
		else:
		    context_dict['allT'] = 0
		    context_dict['hasTesting'] = False
		    context_dict['percentageallT'] = 100.0
		context_dict['progressusers'] = progressusers
		context_dict['progressusersT'] = progressusersT
		if progressusers!=0:
			context_dict['progressavailable'] = True
			context_dict['percentage']=(float(activists)/float(allusers))*100.0
		else:
			context_dict['progressavailable'] = False
			context_dict['percentage']=100.0
		if progressusersT!=0:
			context_dict['progressTavailable'] = True
		else:
			context_dict['progressTavailable'] = False
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
		    chapter.url = chapter.title.replace(':','_111_').replace('=','_121_').replace('&', '_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'', '_001_')
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
	hasCat = True
	hasQuiz = True
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		chapter_tl = chapter_title.replace('_111_',':').replace('_121_','=').replace('_131_','&').replace('_141_','(').replace('_142_',')').replace('_151_','[').replace('_152_',']').replace('_001_','\'').replace('_', ' ')
		try:
		    chapt = Chapter.objects.get(title = chapter_tl)
		    pages = Page.objects.filter(chapter = chapt)
		    pages = pages.order_by('number')
		    context_dict['chapter'] = chapter_title
		    context_dict['c'] = chapt
		    context_dict['title'] = chapter_tl
		    context_dict['pages'] = pages
		    for page in pages:
		        page.url = page.title.replace(':','_111_').replace('=','_121_').replace('&', '_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		    try:
		        quiz_cat = chapt.quiz_category
		        quizzes = Quiz.objects.filter(category = quiz_cat)
		        context_dict['quizzes'] = quizzes
		    except Category.DoesNotExist:
		        hasCat = False
		        hasQuiz = False
		    except Quiz.DoesNotExist:
		        hasQuiz = False
		except Chapter.DoesNotExist:
		    exists = False
		chapters = Chapter.objects.order_by('title')
		for chapter in chapters:
			chapter.url = chapter.title.replace(':','_111_').replace('=','_121_').replace('&', '_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		context_dict['hasQuiz'] = hasQuiz
		context_dict['hasCat'] = hasCat
		context_dict ['chapters'] = chapters
		context_dict['exists'] = exists

	return render(request, 'trainingPortal/chapter.html', context_dict)
def page(request,chapter_title,page_title):
    context_dict = {}
    exists = True
    hasNext = False
    hasPrevious = False
    hasExercise = False
    hasDiagram = True
    hasMultiple = True
    isFurtherReading = False
    chapNum=0
    if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		title= page_title.replace('_111_',':').replace('_121_','=').replace('_131_','&').replace('_141_','(').replace('_142_',')').replace('_151_','[').replace('_152_',']').replace('_001_','\'').replace('_', ' ')
		chapter_tl = chapter_title.replace('_111_',':').replace('_121_','=').replace('_131_','&').replace('_141_','(').replace('_142_',')').replace('_151_','[').replace('_152_',']').replace('_001_','\'').replace('_', ' ')
		print title
		print chapter_tl
		try:
		    chapt = Chapter.objects.get(title = chapter_tl)
		    page = Page.objects.get(chapter = chapt, title = title)
		    chapNum = chapt.number
		    mode = page.learningStyleMode
		    user = request.user
		    profile = user.profile
		    testing = getMode()
		    context_dict['testing'] = testing
		    if testing:
		        try:
		            exercises = PageExercise.objects.get(chapter = chapt,page = page)
		            hasExercise = True
		            if profile.testingType == '0':
		                e = exercises.Default_Exercise_id
		                if not e.disableMode and not e.multipleMode and not e.furtherReadingMode and not e.diagramMode :
		                        hasExercise = False
		                if e.disableMode:
		                        hasExercise = False
		                if e.furtherReadingMode:
		                    isFurtherReading = True
		                context_dict ['exercise'] = e
		                if e.multipleMode:
		                    hasMultiple = True
		                else:
		                    hasMultiple = False

		                    if e.diagramMode:
		                        hasDiagram = True
		                    else:
		                        hasDiagram = False
		            else:
		                EXERCISE_TYPES = {'1':exercises.exercise_Activist_id, '2':exercises.exercise_Reflector_id, '3':exercises.exercise_Theorist_id, '4':exercises.exercise_Pragmatist_id }
		                e = EXERCISE_TYPES.get(profile.learningType)
		                context_dict ['exercise'] = e
		                if not e.disableMode and not e.multipleMode and not e.furtherReadingMode and not e.diagramMode :
		                        hasExercise = False
		                if e.disableMode:
		                        hasExercise = False
		                if e.furtherReadingMode:
		                    isFurtherReading = True
		                if e.multipleMode:
		                    hasMultiple = True
		                else:
		                    hasMultiple = False
		                    if e.diagramMode:
		                        context_dict ['diagram'] = e.diagram
		                        hasDiagram = True
		                    else:
		                        hasDiagram = False

		        except PageExercise.DoesNotExist:
		            hasExercise = False
		        except Exercise.DoesNotExist:
		             hasExercise = False
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
		            try:
		                exercises = PageExercise.objects.get(chapter = chapt,page = page)
		                hasExercise = True
		                EXERCISE_TYPES = {'1':exercises.exercise_Activist_id, '2':exercises.exercise_Reflector_id, '3':exercises.exercise_Theorist_id, '4':exercises.exercise_Pragmatist_id }
		                e = EXERCISE_TYPES.get(profile.learningType)
		                context_dict ['exercise'] = e
		                if not e.disableMode and not e.multipleMode and not e.furtherReadingMode and not e.diagramMode :
		                        hasExercise = False
		                if e.disableMode:
		                        hasExercise = False
		                if e.furtherReadingMode:
		                    isFurtherReading = True
		                if e.multipleMode:
		                    hasMultiple = True
		                else:
		                    hasMultiple = False
		                    if e.diagramMode:
		                        context_dict ['diagram'] = e.diagram
		                        hasDiagram = True
		                    else:
		                        hasDiagram = False
		            except PageExercise.DoesNotExist:
		                hasExercise = False
		            except Exercise.DoesNotExist:
		                hasExercise = False
		            ENTRY_TYPES = {'1':page.entry_Activist_Type, '2':page.entry_Reflector_Type, '3':page.entry_Theorist_Type, '4':page.entry_Pragmatist_Type }
		            context_dict['entry'] = ENTRY_TYPES.get(profile.learningType)
		        else:
		            try:
		                exercises = PageExercise.objects.get(chapter = chapt,page = page)
		                hasExercise = True
		                e = exercises.exercise_Default_id
		                context_dict ['exercise'] = e
		                if e.disableMode:
		                        hasExercise = False

		                if not e.disableMode and not e.multipleMode and not e.furtherReadingMode and not e.diagramMode :
		                        hasExercise = False
		                if e.furtherReadingMode:
		                    isFurtherReading = True
		                if e.multipleMode:
		                    hasMultiple = True
		                else:
		                    hasMultiple = False
		                    if e.diagramMode:
		                        hasDiagram = True
		                        context_dict ['diagram'] = e.diagram
		                    else:
		                        hasDiagram = False
		            except PageExercise.DoesNotExist:
		                hasExercise = False
		            except Exercise.DoesNotExist:
		                hasExercise = False
		            context_dict ['entry'] = page.entry_default
		    context_dict ['chapter_url'] = chapter_title
		    context_dict ['chapter'] = chapter_tl
		    context_dict ['chapter_number'] = chapNum
		    context_dict ['title'] = title
		    context_dict ['page'] = page
		    pages = Page.objects.filter(chapter = chapt)
		    numberofPages = Page.objects.filter(chapter = chapt).count()
		    context_dict ['count'] = numberofPages
		    current = page.number
		    if numberofPages > 1:
		        if current == numberofPages:
		            hasPrevious=True
		            n = numberofPages - 1
		            try:
		                previous = Page.objects.get(chapter = chapt,number=n)
		                pt = previous.title
		                context_dict['previous'] = pt.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		            except Page.DoesNotExist:
		                hasPrevious = False
		        elif current == numberofPages-1:
		            hasNext=True
		            next = Page.objects.get(chapter = chapt,number=numberofPages)
		            nt=next.title
		            context_dict['next'] = nt.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		            if current>1:
		                hasPrevious=True
		                n = current - 1
		                try:
		                    previous = Page.objects.get(chapter = chapt,number=n)
		                    pt = previous.title
		                    context_dict['previous'] = pt.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		                except Page.DoesNotExist:
		                    hasPrevious = False
		        elif current==1:
		            hasNext=True
		            n = current + 1
		            try:
		                next = Page.objects.get(chapter = chapt,number=n)
		                nt = next.title
		                context_dict['next'] = nt.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		            except Page.DoesNotExist:
		                hasNext = False
		        else:
		            hasNext=True
		            n = current + 1
		            try:
		                next = Page.objects.get(chapter = chapt,number=n)
		                nt = next.title
		                context_dict['next'] = nt.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		            except Page.DoesNotExist:
		                hasNext = False
		            hasPrevious=True
		            p = current - 1
		            try:
		                previous = Page.objects.get(chapter = chapt,number=p)
		                pt = previous.title
		                context_dict['previous'] = pt.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		            except Page.DoesNotExist:
		                hasPrevious = False
		    context_dict ['pages'] = pages
		    for page in pages:
		        page.url = page.title.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		except Page.DoesNotExist:
		    exists= False
		    print 'Page not Found'
		except Chapter.DoesNotExist:
		    exists= False
		    print 'Chapter not Found'
		chapters = Chapter.objects.order_by('title')
		for chapter in chapters:
		    chapter.url = chapter.title.replace(':','_111_').replace('=','_121_').replace('&','_131_').replace(' ', '_').replace('(', '_141_').replace(')', '_142_').replace('[','_151_').replace(']', '_152_').replace('\'','_001_')
		context_dict ['chapters'] = chapters
		context_dict['exists'] = exists
		context_dict['hasExercise'] = hasExercise
		context_dict['hasDiagram'] = hasDiagram
		context_dict['hasMultiple'] = hasMultiple

		context_dict['hasNext'] = hasNext
		context_dict['hasPrevious'] = hasPrevious
		context_dict['furtherReading']	= isFurtherReading
    return render(request, 'trainingPortal/page.html', context_dict)

def profile(request,username):
	context_dict = {"username" : username}
	exists = True
	personal = False
	pro = True
	testing = getMode()
	ranking = 'Novice'

	context_dict['testing'] = testing
	if request.user.is_authenticated():
		context_dict['set_learningType'] = completedLearningStyle(request.user)
		if request.user.username == username:
		    personal = True
		    try:
		        progress = Progress.objects.get(user=request.user)
		        str = progress.score
		        val = str.split(',')
		        size = len(val)-1
		        times = size / 3
		        t=0
		        ignore='Example' #category
		        while t<size-1:
		            if val[t].lower() == ignore.lower():
		                times = times - 1
		                break;
		            t=t+3
		        t=0
		        a=0
		        scores =[[{}] for t in range(0,times) ]
		        quizCount=0


		        sum = 0.0
		        valid=0
		        while t<size-1:

		            if val[t].lower() != ignore.lower():
		                cat = Category.objects.get(category=val[t])
		                quizzes = Quiz.objects.filter(category=cat)
		                q=0
		                qsum=0.0
		                for quiz in quizzes:
		                    sitting = Sitting.objects.filter(user=request.user, quiz=quiz, testing=False).order_by('-end')[:1]
		                    if sitting.count()>0:
		                        percentage =  sitting[0].get_percent_correct
		                        qsum=qsum+percentage
		                        q=q+1
		                        quizCount=quizCount+1
		               # qz = Quiz.objects.get(title=val[t])
		                percent = 0.0
		                if q>0:
		                    percent = (float(qsum / q)/float(100))*100.0
		                sum = sum + percent
		                score = [{'chapter': val[t], 'correct': val[t+1], 'all':val[t+2],'percentage':percent}]
		                scores[a]=score
		                a=a+1
		                valid=valid+1
		            t=t+3
		            if a == times:
		                break

		        if sum!=0.0:
		             context_dict['average'] = sum / times
		        else:
		             context_dict['average'] = sum
		             if valid==0:
		                 pro = False

		        context_dict['scores'] = scores
		        color='blue'
		        if quizCount>0 and quizCount<6:
		            ranking='Beginner'
		            color='green'
		        elif quizCount>5 and quizCount<15:
		            ranking='Advanced Learner'
		            color='orange'
		        elif  quizCount>15:
		            ranking='Expert'
		            color='red'

		        context_dict['ranking'] = ranking
		        context_dict['rankingColor'] = color
		        context_dict['quizCount'] = quizCount


		    except Progress.DoesNotExist:
		        pro = False
		context_dict['hasprogress'] = pro
		quizCount=0
		ranking='Novice'
		color='blue'
		try:

			usr = User.objects.get(username = username)
			if personal:
				context_dict['usr'] = usr
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
				try:
				    progress = Progress.objects.get(user=usr)
				    str = progress.score
				    val = str.split(',')
				    size = len(val)-1
				    times = size / 3
				    t=0
				    ignore='Example' #category
				    while t<size-1:
				        if val[t].lower() == ignore.lower():
				            times = times - 1
				            break;
				        t=t+3
				    t=0
				    a=0
				    scores =[[{}] for t in range(0,times) ]

				    sum = 0.0
				    valid=0
				    while t<size-1:
				        if val[t].lower() != ignore.lower():
				            cat = Category.objects.get(category=val[t])
				            quizzes = Quiz.objects.filter(category=cat)
				            for quiz in quizzes:
				                sitting = Sitting.objects.filter(user=usr, quiz=quiz).order_by('-end')[:1]
				                if sitting.count()>0:
				                    quizCount=quizCount+1
				            a=a+1
				            valid=valid+1
				        t=t+3
				        if a == times:
				            break

				    if quizCount>0 and quizCount<6:
				        ranking='Beginner'
				        color='green'
				    elif quizCount>5 and quizCount<15:
				        ranking='Advanced Learner'
				        color='orange'
				    elif  quizCount>15:
				        ranking='Expert'
				        color='red'

				except Progress.DoesNotExist:
				    pro = False
				context_dict['ranking'] = ranking
				context_dict['rankingColor'] = color
			except Profile.DoesNotExist:
				exists = False
		except User.DoesNotExist:
			exists = False

	context_dict['exists'] = exists
	context_dict['personal'] = personal
	return render(request, 'trainingPortal/profile.html', context_dict)
def completedLearningStyle(user):
	if (user.profile.learningType == '0'):
		return False
	else :
		return True