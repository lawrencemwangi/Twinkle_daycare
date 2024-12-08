from django.db import models

# Create your models here.

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name
    