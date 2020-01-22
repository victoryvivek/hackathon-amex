from django.contrib import admin
from tryapp import models

# Register your models here.


class TemplateInfoAdmin(admin.ModelAdmin):
    change_list_template = 'admin/tryapp/template_info/template_info_change.html'

admin.site.register(models.TemplateInfo, TemplateInfoAdmin)
