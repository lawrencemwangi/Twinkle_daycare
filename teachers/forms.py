from django import forms
from .models import Child, Parent, HealthRecord

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['allergies', 'medication', 'medical_conditions']

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'date_of_birth', 'parent', 'health_record']

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        age = self.calculate_age(dob)
        self.cleaned_data['age'] = age
        return dob

    def calculate_age(self, dob):
        from datetime import date
        today = date.today()
        age = today.year - dob.year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1
        return age
