from django.shortcuts import render

from .models import Student, Semester


# Create your views here.
def index(req):
    return render(req, 'index.html')


def semesters(req):
    semesters = Semester.objects.all()
    s_sem1 = Student.objects.filter(semester='1')
    s_sem2 = Student.objects.filter(semester='2')
    s_sem3 = Student.objects.filter(semester='3')
    s_sem4 = Student.objects.filter(semester='4')
    s_sem5 = Student.objects.filter(semester='5')
    s_sem6 = Student.objects.filter(semester='6')
    students = [len(s_sem1), len(s_sem2), len(s_sem3), len(s_sem4), len(s_sem5), len(s_sem6)]
    context = {'values': zip(semesters, students)}
    return render(req, 'semester_list.html', context)


def subjects(req):
    return render(req, 'subjects_list.html')


def students(req):
    return render(req, 'student_list.html')
