from django.contrib import admin
from .models import Teacher
from .models import Section
from .models import Subject
from .models import Course
from .models import SchoolYear


class CourseAdmin(admin.ModelAdmin):
    list_display = ('section', 'subject', 'teacher', 'schedule')
    list_filter = ['section__level', 'subject', 'section', 'teacher']

admin.site.register(Teacher)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(SchoolYear)
admin.site.register(Course, CourseAdmin)
