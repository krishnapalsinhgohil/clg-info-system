from django.contrib import admin

from home.models import Student, Semester, Subject

# Register your models here.

admin.site.register([Student, Semester, Subject])
