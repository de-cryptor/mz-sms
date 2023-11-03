# yourapp/management/commands/import_students_csv.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.student.models import *

class Command(BaseCommand):
    help = 'Course to Session Migration'

    def handle(self, *args, **kwargs):
        
        courses = Course.objects.all()
        for course in courses:
            session = Session.objects.create(
                name=f'{course.name} - 2023 - I',
                course=course,
                mode='Offline',
            )
            print(session)
            students = StudentCourse.objects.filter(course=course)
            for student in students:
                enrollment = SessionEnrollment.objects.create(
                    session=session,
                    student=student.student,
                )
                print(enrollment)
