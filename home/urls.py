from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('semesters/', views.semesters, name="semester"),
    path('subjects/', views.subjects, name="subject"),
    path('students/', views.students, name="student"),
    path('homeadmin/', views.home_admin, name="adminhome"),
    path('semester/', views.add_semester, name="a_semester"),
    path('subject/', views.add_subject, name="a_subject"),
    path('student/', views.add_student, name="a_student"),
    path('insertsem', views.ins_sem, name="ins_semester"),
    path('insertsub', views.ins_subject, name="ins_subject"),
    path('insertst/', views.ins_student, name="ins_student"),
    path('stud_operation/', views.perform_stud_operation, name="stud_operations"),
    path('sub_operation/', views.perform_sub_operation, name="sub_operations"),
    path('upd_student/', views.upd_student, name="upd_student"),
    path('upd_subject/', views.upd_subject, name="upd_subject"),
]
