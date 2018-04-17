from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentForm, SemesterForm, SubjectForm
from .models import Student, Semester, Subject


# Create your views here.
def index(req):
    return render(req, 'index.html')


def semesters(req):
    numbers = []
    for x in Semester.objects.all():
        numbers.append(len(Student.objects.filter(semester=x.id)))
    context = {'values': zip(Semester.objects.all(), numbers)}
    return render(req, 'semester_list.html', context)


def subjects(req):
    subjects = Subject.objects.all()
    return render(req, 'subjects_list.html', {'subjects': subjects})


def students(req):
    students = Student.objects.all()
    return render(req, 'student_list.html', {'students': students})


def home_admin(req):
    return render(req, 'home_admin/index.html')


def add_semester(req):
    return render(req, 'home_admin/add_semester.html', {'form': SemesterForm})


def ins_sem(req):
    name = req.POST["semester_name"]
    credits = req.POST.get('credits')
    Semester.objects.create(sem_name=name, credits=credits)
    return HttpResponse("Inserted Successfully")


def add_student(req):
    return render(req, 'home_admin/add_student.html', {'form': StudentForm})


def ins_student(req):
    name = req.POST.get('name')
    id = req.POST.get('semester')
    semester = Semester.objects.get(id=id)
    Student.objects.create(name=name, semester=semester)
    return HttpResponse("Inserted Successfully")


def perform_stud_operation(req):
    id = req.POST.get("id")
    if req.POST.get("btnDelete"):
        s = Student.objects.get(id=id)
        s.delete()
        return HttpResponseRedirect("/home/students/")
    elif req.POST.get("btnUpdate"):
        s = Student.objects.get(id=id)
        context = {"id": id, "form": StudentForm(initial={'name': s.name, 'semester': s.semester})}
        return render(req, 'upd_student.html', context)


def upd_student(req):
    id = req.POST.get("id")
    name = req.POST.get("name")
    semester_id = req.POST.get("semester")
    semester = Semester.objects.get(id=semester_id)
    s = Student.objects.get(id=id)
    s.name = name
    s.semester = semester
    s.save()
    return HttpResponseRedirect("/home/students")


def add_subject(req):
    return render(req, 'home_admin/add_subject.html', {'form': SubjectForm})


def ins_subject(req):
    name = req.POST.get('name')
    optional = req.POST.get('optional')
    id = req.POST.get('semester')
    semester = Semester.owbjects.get(id=id)
    if optional == 'on':
        Subject.objects.create(name=name, semester=semester, optional=True)
    else:
        Subject.objects.create(name=name, semester=semester, optional=False)

    return HttpResponseRedirect("/home/subjects/")


def perform_sub_operation(req):
    id = req.POST.get("id")
    if req.POST.get("btnDelete"):
        s = Subject.objects.get(id=id)
        s.delete()
        return HttpResponseRedirect("/home/subjects/")
    elif req.POST.get("btnUpdate"):
        s = Subject.objects.get(id=id)
        context = {"id": id,
                   "form": SubjectForm(initial={'name': s.name, 'semester': s.semester, 'optional': s.optional})}
        return render(req, 'upd_subject.html', context)


def upd_subject(req):
    id = req.POST.get("id")
    name = req.POST.get("name")
    optional = req.POST.get("optional")
    semester_id = req.POST.get("semester")
    semester = Semester.objects.get(id=semester_id)
    s = Subject.objects.get(id=id)
    s.name = name
    if optional == 'Yes':
        s.optional = True
    else:
        s.optional = False
    s.semester = semester
    s.save()
    return HttpResponseRedirect("/home/subjects")
