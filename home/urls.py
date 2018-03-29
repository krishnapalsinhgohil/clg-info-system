from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('semesters/',views.semesters,name="semesters"),
    path('subjects/',views.subjects,name="subjects"),
    path('students/',views.students,name="students"),
]
