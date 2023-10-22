# yourapp/management/commands/import_students_csv.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.student.models import Student, Course, StudentCourse

class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', help='Path to the CSV file containing student data')
        parser.add_argument('--course_id', help='Course ID')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        course_id = kwargs['course_id']

        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row if present
                manzil_ids = []
                for row in reader:
                    manzil_id = row[0].strip()
                    manzil_ids.append(manzil_id)
                students = Student.objects.filter(manzil_id__in=manzil_ids)
                print(len(manzil_ids))
                print(len(students))
                course = Course.objects.get(course_id=course_id)
                print(course)
                student_courses = []
                for student in students:
                    try:
                        student_course = StudentCourse(
                            student=student,
                            course=course,
                        )
                        student_courses.append(student_course)
                        # self.stdout.write(self.style.SUCCESS(f'Successfully created student: {student.manzil_id}'))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(str(e)))

                StudentCourse.objects.bulk_create(
                    student_courses,
                )

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {csv_file}'))
