# Generated by Django 3.1.4 on 2020-12-23 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='usn',
        ),
    ]
