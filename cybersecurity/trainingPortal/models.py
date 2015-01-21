from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	profile_pic = FilerImageField(
		blank=True,
		null=True,
		related_name="profile_picture",
		on_delete=models.SET_NULL,  # Important
	)
	def __unicode__(self):
		return self.user.username
		
		
class Chapter(models.Model):
	title = models.CharField(max_length=128, unique=True)


	def __unicode__(self):
		return self.title
		
class Page(models.Model):
	chapter = models.ForeignKey(Chapter)
	title = models.CharField(max_length=256, unique=True)
	content = models.CharField(max_length=1024)
	
	def __unicode__(self):
		return self.title		
