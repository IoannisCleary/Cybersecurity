from django.contrib import admin
from trainingPortal.models import Page,Chapter,Profile,Mode,Exercise,PageExercise


# Register your models here.
admin.site.register(Mode)
admin.site.register(Profile)
admin.site.register(Chapter)

class PageAdmin(admin.ModelAdmin):
	change_form_template = 'trainingPortal/admin/change_form.html'

admin.site.register(Page,PageAdmin)
admin.site.register(Exercise,PageAdmin)
admin.site.register(PageExercise,PageAdmin)