from django.contrib import admin

# Register your models here.
from school.models import School, Teacher, Subject, Department

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Department)
