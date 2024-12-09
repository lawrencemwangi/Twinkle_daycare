from django.db import models
from teachers.models import Enrollment
import uuid


# Create your models here.

class Schoolclass(models.Model):
    class_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name

class Finance(models.Model):
    class_name = models.CharField(max_length=100)
    term = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=10)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    fees_breakdown = models.TextField(blank=True, null=True) 
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.class_name} - {self.term} ({self.academic_year})"


class Invoice(models.Model):
    child = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    date_issued = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)  
    status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')

    def __str__(self):
        return f"Invoice for {self.child} - {self.total_amount} ({self.status})"

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_invoice_number():
        return f"Twinkle-{uuid.uuid4().hex[:5].upper()}"