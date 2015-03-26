from django.contrib import admin
from trainingPortal.models import Section,Chapter,Profile,Mode,Exercise,SectionExercise,Announcement,IndexElement


# Register your models here.
admin.site.register(Mode)
admin.site.register(Profile)

class SectionAdmin(admin.ModelAdmin):
	change_form_template = 'trainingPortal/admin/change_form.html'
	class Media:
	    css = {
	        'all': ('/static/css/custom.css',)
	        }

admin.site.register(Section,SectionAdmin)
admin.site.register(Exercise,SectionAdmin)
admin.site.register(Chapter,SectionAdmin)
admin.site.register(SectionExercise,SectionAdmin)
admin.site.register(Announcement)
admin.site.register(IndexElement,SectionAdmin)