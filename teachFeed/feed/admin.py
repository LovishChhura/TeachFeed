from django.contrib import admin
from .models import Department, Teacher, Subject, Tfeed
# Register your models here.

admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Tfeed)