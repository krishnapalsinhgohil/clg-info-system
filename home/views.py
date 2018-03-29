from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'index.html')


def semesters(req):
    return render(req, 'semester_list.html')


def subjects(req):
    return render(req, 'subjects_list.html')


def students(req):
    return render(req, 'student_list.html')
