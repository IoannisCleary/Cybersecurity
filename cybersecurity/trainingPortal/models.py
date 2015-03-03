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
class Exercise(models.Model):
	chapter = models.ForeignKey(Chapter)
	number = models.IntegerField(default=1,validators=[MinValueValidator(1)],unique=True,help_text="This field is used to sort the exercises. Use a unique number")
	question = models.CharField(max_length=150, default="(Empty)")
	multipleMode =  models.BooleanField(default=False,help_text="If you want to add multiple exercises enable this and in the text field below add both exercises and the available answers")
	diagramMode = models.BooleanField(default=False,help_text="Select to use a diagram instead of text. Used when multipleMode is disabled.")
	furtherReadingMode = models.BooleanField(default=False,help_text="Select to use only the text field without the answer fields.")
	diagram = FilerImageField(
		blank=True,
		null=True,
		related_name="exercise_image"
	)
	text = RichTextField(config_name='awesome_ckeditor',help_text="This field is used instead of a diagram to add information about a question. When multipleMode is enabled this field should contain exercises and the available answers.(Remember to add a number to each exercise + add a letter for each answer)",default="Empty")
	source = models.CharField(max_length=200,default="No source",help_text="This field is used to add source of diagram or question")
	availableAnswers = RichTextField(config_name='awesome_ckeditor',help_text="Used only when multipleMode is disabled. This field displays the available answers to this exercise",default="Empty")
	correctAnswer = RichTextField(config_name='awesome_ckeditor',default="Not available",help_text="This field displays the correct answer and the explanation why. If multipleMode is enabled it will display all the correct answers from the exercises above. (Remember to add a number to each exercise)")
	def __unicode__(self):
		return self.question
	class Meta:
		verbose_name_plural = "Exercises"
		unique_together = (("chapter", "number"),)

class PageExercise(models.Model):
	chapter = models.ForeignKey(Chapter)
	page = models.ForeignKey(Page)
	exercise_Default_id = models.ForeignKey(Exercise,related_name='exercise_Default')
	exercise_Activist_id = models.ForeignKey(Exercise,related_name='exercise_Activist')
	exercise_Reflector_id = models.ForeignKey(Exercise,related_name='exercise_Reflector')
	exercise_Theorist_id = models.ForeignKey(Exercise,related_name='exercise_Theorist')
	exercise_Pragmatist_id = models.ForeignKey(Exercise,related_name='exercise_Pragmatist')
	def __unicode__(self):
		return self.chapter.title +' - '+self.page.title
	class Meta:
		verbose_name_plural = "PageExercises"
		unique_together = (("chapter","page"),)