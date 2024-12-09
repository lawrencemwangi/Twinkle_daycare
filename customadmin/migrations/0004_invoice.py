# Generated by Django 5.0.2 on 2024-12-09 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0003_finance'),
        ('teachers', '0009_rename_reason_absent_attendance_reason_absent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(editable=False, max_length=20, unique=True)),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=50)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.enrollment')),
            ],
        ),
    ]
