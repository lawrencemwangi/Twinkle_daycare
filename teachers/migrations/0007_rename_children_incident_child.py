# Generated by Django 5.0.2 on 2024-12-09 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_alter_incident_children'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='children',
            new_name='child',
        ),
    ]
