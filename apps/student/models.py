from django.db import models

# Create your models here.

class Student(models.Model):
    
    manzil_id = models.CharField(unique=True, null=False, blank=False, max_length=255)
    name = models.CharField(null=False, blank=False, max_length=255)
    date_of_birth = models.DateField(null=False, blank=False)

    def __str__(self) -> str:
        return str(self.manzil_id)