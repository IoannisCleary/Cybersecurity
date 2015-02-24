from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MinValueValidator

from ckeditor.fields import RichTextField

LEARNING_TYPES = ( ('0','Not selected'), ('1','Activist'), ('2','Reflector'), ('3','Theorist'), ('4','Pragmatist'), )
TESTING_TYPES = ( ('0','A'), ('1','B'))

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
	learningType = models.CharField(max_length=1,default='0',choices=LEARNING_TYPES)
	testingType =  models.CharField(max_length=1,default='0',choices=TESTING_TYPES)
	def __unicode__(self):
		return self.user.username
class Mode(models.Model):
	name =  models.CharField(max_length=50)
	enable = models.BooleanField(default=False,help_text="Select to enable Testing Mode where type A users see only default parts of chapters and type B users see learning style specific parts of chapters")
	def __unicode__(self):
		return self.name


class Chapter(models.Model):
	number = models.IntegerField(default=1,validators=[MinValueValidator(1)],unique=True,help_text="This field is used to sort the chapters. Use a unique number")
	title = models.CharField(max_length=128, unique=True)
	overview = models.CharField(max_length=500,default="Not available")
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Chapters"

class Page(models.Model):
	chapter = models.ForeignKey(Chapter)
	number = models.IntegerField(default=1,validators=[MinValueValidator(1)],help_text="This field is used to sort the pages. Use a unique number")
	title = models.CharField(blank=False,max_length=256)
	entry_default = RichTextField(config_name='awesome_ckeditor',help_text="This field is displayed when learningStyleMode is disabled.",default="Empty")
	learningStyleMode = models.BooleanField(default=True,help_text="Select to enable Learning Style Mode based on Honey & Mumfords learning styles and use the entry fields below. Disable to use default entry field above")
	entry_Activist_Type = RichTextField(config_name='awesome_ckeditor',help_text="This field is displayed when learningStyleMode is enabled. Activist specific content",default="Empty")
	entry_Reflector_Type = RichTextField(config_name='awesome_ckeditor',help_text="This field is displayed when learningStyleMode is enabled. Reflector specific content",default="Empty")
	entry_Theorist_Type = RichTextField(config_name='awesome_ckeditor',help_text="This field is displayed when learningStyleMode is enabled. Theorist specific content",default="Empty")
	entry_Pragmatist_Type = RichTextField(config_name='awesome_ckeditor',help_text="This field is displayed when learningStyleMode is enabled. Pragmatist specific content",default="Empty")
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Pages"
		unique_together = (("chapter", "number"),)