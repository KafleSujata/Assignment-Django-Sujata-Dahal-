from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student,Department

# Create your views here.

def home(request):
    return render(request,'home.html')


def students(request):
    students=Student.objects.all().values()
    template=loader.get_template('students.html')
    context={
        'students':students,
    }

    return HttpResponse(template.render(context,request))


def department(request):
    department=Department.objects.all().values()
    template=loader.get_template('department.html')
    context={
        'department':department,
    }
    return HttpResponse(template.render(context,request))