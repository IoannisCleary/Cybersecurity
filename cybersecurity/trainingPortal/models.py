from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

from ckeditor.fields import RichTextField

LEARNING_TYPES = ( ('0','Not selected'), ('1','Activist'), ('2','Reflector'), ('3','Theorist'), ('4','Pragmatist'), )

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
		unique_together = (("chapter", "title"),)