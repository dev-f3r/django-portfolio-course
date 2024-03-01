from django.contrib import admin

from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "summary", )

admin.site.register(Job, JobAdmin)
