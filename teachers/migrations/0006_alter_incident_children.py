# Generated by Django 5.0.2 on 2024-12-09 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_incident_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.enrollment'),
        ),
    ]
