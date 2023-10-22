# yourapp/management/commands/import_students_csv.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.student.models import Student

class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--csv_file', help='Path to the CSV file containing student data')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row if present

                for row in reader:
                    name, dob_str = row
                    try:
                        dob = datetime.strptime(dob_str, '%m/%d/%Y').date()
                        manzil_id = name.split(' ')[0].upper() + '-' + dob.strftime("%d-%m-%Y")
                        try:
                            Student.objects.create(name=name.title(), date_of_birth=dob, manzil_id=manzil_id)
                        except:
                            pass
                        self.stdout.write(self.style.SUCCESS(f'Successfully created student: {name.title()} : {dob.strftime("%m/%d/%Y")}'))
                    except ValueError:
                        self.stderr.write(self.style.ERROR(f'Invalid date format for {name}: {dob_str}'))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {csv_file}'))
