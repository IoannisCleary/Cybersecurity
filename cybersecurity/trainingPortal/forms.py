from django import forms
from trainingPortal.models import Profile
from random import randint
from django.contrib.auth.models import User

class LearningTypeForm(forms.ModelForm):
	#LEARNING_TYPES = (('1','Activist'), ('2','Reflector'), ('3','Theorist'), ('4','Pragmatist'), )
	#type = forms.ChoiceField(choices=LEARNING_TYPES, required=True, label="Enter learning type: ")
	class Meta:
		model = Profile
		fields = ('learningType',)
		exclude = ('age','profile_pic','user')
		
class RegisterForm(forms.Form):
	username = forms.CharField(max_length=25, label='Username (Note = Do not use real name.')
	age = forms.IntegerField(label='Age')
	def signup(self, request, user):
		user.username = self.cleaned_data['username']
		profile = Profile()
		random = randint(1,50)
		print random
		if random>25:
			type="A"
		else:
			type="B"
		print type
		profile.user = user
		profile.testingType=type
		profile.age = self.cleaned_data['age']
		profile.save();
		user.profile = profile
		user.save()
		
	