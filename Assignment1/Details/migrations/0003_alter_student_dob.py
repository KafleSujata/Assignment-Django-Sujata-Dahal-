# Generated by Django 4.1 on 2022-08-22 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0002_rename_semister_number_student_semester_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(),
        ),
    ]
