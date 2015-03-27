# References for the creation of this population script:
#	Tango with Django Book 1.7
#	2013
#	Leif Azzopardi and David Maxwel
#	Available at: http://www.tangowithdjango.com/book17/chapters/models.html#creating-a-population-script

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cybersecurity.settings')

import django
django.setup()

from trainingPortal.models import *
from django.contrib.auth.models import User

def setup():
	
	create_profile('admin')
	testing_mode()
	overview='<p>This chapter starts with a general introduction to what Spam is, what Spammers aim to achieve, how they achieve it and what is the role of a user in a spam related attack. It will mainly focus on Phishing threats.</p>'
	chapt=create_chapter(1,'Spam',overview)
	
	create_section_default(chapt,1,'Introduction','Enter content of section1HTML.txt',False)
	create_section_default(chapt,2,'Phishing','Enter content of section2HTML.txt',False)
	create_section_default(chapt,3,'Android Permissions','Enter content of section3HTML.txt',False)
	section = create_section(chapt,4,'Spam Detection','Enter content of section4HTML.txt in all fields',True,'Enter content of section4HTML.txt in all fields','Enter content of section4HTML.txt in all fields','Enter content of section4HTML.txt in all fields','Enter content of section4HTML.txt in all fields')
	create_section_default(chapt,5,'How To Stay Safe','Enter content of section5HTML.txt',False)
	exP = create_exercise(False,chapt,1,"Spam Checker - Pragmatists",False,False,True)
	exA = create_exercise(False,chapt,2,"Spam Checker - Activist",True,False,False)
	exR = create_exercise(False,chapt,3,"Spam Checker - Reflector",False,False,True)
	exT = create_exercise(False,chapt,4,"Spam Checker - Theorist",False,False,True)
	exNo = create_exercise(True,chapt,5,"No Exercise",False,False,False)
	sectexercise = create_section_exercise(chapt,section,exNo,exP,exA,exR,exT)
	print "Done."


def create_profile(name):
    user = User.objects.get_or_create(username=name)[0]
    profile = Profile.objects.get_or_create(user=user,age=0,learningStyle='0',testingType='0')[0]
    return user
def create_chapter(number,title,overview):
    chapt = Chapter.objects.get_or_create(number=number,title=title,overview=overview)[0]
    return chapt
def create_section(chapter,number,title,entry_default,learningStyleMode,entry_Activist_Type,entry_Reflector_Type,entry_Theorist_Type,entry_Pragmatist_Type):
    sect = Section.objects.get_or_create(chapter=chapter,number=number,title=title,entry_default=entry_default,learningStyleMode=learningStyleMode,entry_Activist_Type=entry_Activist_Type,entry_Reflector_Type=entry_Reflector_Type,entry_Theorist_Type=entry_Theorist_Type,entry_Pragmatist_Type=entry_Pragmatist_Type)[0]
    return sect
def create_section_default(chapter,number,title,entry_default,learningStyleMode):
    sect = Section.objects.get_or_create(chapter=chapter,number=number,title=title,entry_default=entry_default,learningStyleMode=learningStyleMode)[0]
    return sect
def create_exercise(disable,chapter,number,question,multiple,diagram,further):
    ex = Exercise.objects.get_or_create(disableMode=disable,chapter=chapter,number=number,question=question,multipleMode=multiple,diagramMode=diagram,furtherReadingMode=further,text="Enter content from TXT file with the question name")[0]
    return ex
def create_section_exercise(chapter,section,default,pragmatist,activist,reflector,theorist):
    sectex = SectionExercise.objects.get_or_create(chapter=chapter,section=section,exercise_Default_id=default,exercise_Activist_id=activist,exercise_Reflector_id=reflector,exercise_Theorist_id=theorist,exercise_Pragmatist_id=pragmatist)[0]
    return sectex
def testing_mode():
    mode = Mode.objects.get_or_create(name='testing',enable=False)[0]
    return mode

# Start execution here!
if __name__ == '__main__':
    print "Initializing database"
    setup()