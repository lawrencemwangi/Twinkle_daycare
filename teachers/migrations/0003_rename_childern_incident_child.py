# Generated by Django 5.0.2 on 2024-12-08 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_incident'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='childern',
            new_name='child',
        ),
    ]
