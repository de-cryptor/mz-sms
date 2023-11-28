# yourapp/management/commands/import_students_csv.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.student.models import *

class Command(BaseCommand):
    help = 'Update student Manzil ID format'

    def handle(self, *args, **kwargs):
        
        students = Student.objects.all()
        for student in students:
            manzil_id = student.manzil_id.split('-')
            new_manzil_id = manzil_id[0].title() + '.' + manzil_id[3][2:] + '.' + manzil_id[2] + '.' + manzil_id[1]
            print(manzil_id, new_manzil_id)
            student.manzil_id = new_manzil_id
            student.save()