from django.contrib import admin
from .models import StudentDetail

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','published','bio','github_url')

admin.site.register(StudentDetail,StudentAdmin)

