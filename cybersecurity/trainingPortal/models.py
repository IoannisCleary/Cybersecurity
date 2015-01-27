from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	profile_pic = FilerImageField(
		blank=True,
		null=True,
		related_name="profile_picture",
		on_delete=models.SET_NULL,  # Important
	)
	age = models.IntegerField()
	admin = models.BooleanField(default=False)
	type = models.CharField(max_length=128,default="not selected")
	def __unicode__(self):
		return self.user.username	
		
class Chapter(models.Model):
	title = models.CharField(max_length=128, unique=True)
	
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Chapters"		
		
class Page(models.Model):
	chapter = models.ForeignKey(Chapter)
	title = models.CharField(max_length=256)
	entry = RichTextField(config_name='awesome_ckeditor')
	
	def __unicode__(self):
		return self.title		
	class Meta:
		verbose_name_plural = "Pages"
		unique_together = (("chapter", "title"),)