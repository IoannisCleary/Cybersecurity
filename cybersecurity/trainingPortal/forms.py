from django import forms
from trainingPortal.models import Profile
from random import randint
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=25, label='Username (Note = Do not use real name.')
	age = forms.IntegerField(label='Age')
	def signup(self, request, user):
		user.username = self.cleaned_data['username']
		profile = Profile()
		random = randint(1,50)
		print random
		if rand>25:
			type="A"
		else:
			type="B"
		print type
		profile.user = user
		profile.type=type
		profile.age = self.cleaned_data['age']
		profile.save();
		user.profile = profile
		user.save()
	