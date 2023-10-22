from django.db import models

# Create your models here.

class Student(models.Model):
    
    manzil_id = models.CharField(unique=True, null=False, blank=False, max_length=255)
    name = models.CharField(null=False, blank=False, max_length=255)
    date_of_birth = models.DateField(null=False, blank=False)

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
