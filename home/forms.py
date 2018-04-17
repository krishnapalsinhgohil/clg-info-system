from django import forms

from .models import Semester


class SemesterForm(forms.Form):
    semester_name = forms.CharField(max_length=50)
    credits = forms.IntegerField()


class StudentForm(forms.Form):
    name = forms.CharField(max_length=30)
    semester = forms.ModelChoiceField(Semester.objects.all(), empty_label="Select one!")


class SubjectForm(forms.Form):
    name = forms.CharField(max_length=30)
    optional = forms.NullBooleanField(required=False)
    semester = forms.ModelChoiceField(Semester.objects.all(), empty_label="Select one!")
