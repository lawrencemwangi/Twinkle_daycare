from django.db import models
from authuser.models import CustomUser
from datetime import date

# Create your models here.

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name



class Enrollment(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    ENROLLMENT_STATUS_CHOICES = (
        ('ENROLLED', 'Enrolled'),
        ('PENDING', 'Pending'),
        ('WITHDRAWN', 'Withdrawn'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(null=True, blank=True)
    admission_number = models.CharField(max_length=20, unique=True)
    allergies = models.TextField(null=True, blank=True)  
    medication = models.TextField(null=True, blank=True) 
    medical_conditions = models.TextField(null=True, blank=True)
    grade = models.CharField(max_length=20)
    emg_contact = models.CharField(max_length=15, null=True, unique=True)
    enrollment_status = models.CharField(max_length=10,choices=ENROLLMENT_STATUS_CHOICES,default='PENDING')
    
    parent = models.ForeignKey(
        'authuser.CustomUser',
        on_delete=models.CASCADE,
        limit_choices_to={'user_level': 'parent'},
    )

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    