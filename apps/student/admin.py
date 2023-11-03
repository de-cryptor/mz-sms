from django.contrib import admin
from apps.student.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
# admin.site.register(StudentCourse)
admin.site.register(Session)
admin.site.register(SessionEnrollment)
admin.site.register(Scholarship)
admin.site.register(ScholarshipEnrollment)
admin.site.register(ManzilEvent)
admin.site.register(ManzilEventAttendee)