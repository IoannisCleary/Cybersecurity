from django.contrib import admin
from trainingPortal.models import Page,Chapter,Profile

# Register your models here.
admin.site.register(Chapter)
admin.site.register(Profile)

class PageAdmin(admin.ModelAdmin):
    change_form_template = 'trainingPortal/admin/change_form.html'

admin.site.register(Page,PageAdmin)