# Generated by Django 5.0.2 on 2024-12-09 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_rename_childern_incident_child'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='child',
            new_name='children',
        ),
    ]