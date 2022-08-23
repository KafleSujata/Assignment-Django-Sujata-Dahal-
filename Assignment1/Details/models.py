from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    dob=models.DateField()
    roll_number=models.IntegerField()
    department_name=models.CharField(max_length=255)
    course_name=models.CharField(max_length=255)
    semester_number=models.IntegerField()

class Department(models.Model):
    department_name=models.CharField(max_length=255)
    course_number=models.IntegerField()
    teacher_number=models.IntegerField()