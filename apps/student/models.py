from django.db import models

# Create your models here.

class Student(models.Model):
    
    manzil_id = models.CharField(unique=True, null=False, blank=False, max_length=255)
    name = models.CharField(null=False, blank=False, max_length=255)
    date_of_birth = models.DateField(null=False, blank=False)
    biography = models.TextField(default='')

    def __str__(self) -> str:
        return str(self.manzil_id)

class Course(models.Model):

    course_id = models.CharField(unique=True, null=False, blank=False, max_length=255)
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self) -> str:
        return str(self.course_id)

class StudentCourse(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.student.manzil_id) + '-' + str(self.course.course_id)


class Session(models.Model):

    MODE_CHOICES = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    )

    name = models.CharField(max_length=255, null=False, blank=False)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self) -> str:
        return str(self.name)


class SessionEnrollment(models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.student.manzil_id) + '-' + str(self.session.course.course_id)


class Scholarship(models.Model):
    scholarship_id = models.CharField(max_length=20, unique=True, blank=False, null=False)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.scholarship_id) + '-' + str(self.name)


class ScholarshipEnrollment(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return str(self.scholarship.scholarship_id) + '-' + str(self.student.name)
    

class ManzilEvent(models.Model):
    event_id = models.CharField(max_length=20, unique=True, blank=False, null=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.CharField(max_length=255)
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return str(self.event_id) + '-' + str(self.name)
    

class ManzilEventAttendee(models.Model):
    event = models.ForeignKey(ManzilEvent, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return str(self.event) + '-' + str(self.student.name)