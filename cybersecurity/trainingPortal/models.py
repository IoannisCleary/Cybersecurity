from django.db import models

# Create your models here.

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
