from django.db import models


class Semester(models.Model):
    sem_name = models.CharField(max_length=20)
    credits= models.IntegerField()
    def __str__(self):
        return self.sem_name


class Student(models.Model):
    name = models.CharField(max_length=40)
    semester = models.ForeignKey(Semester, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=40)
    optional = models.BooleanField()
    semester = models.ForeignKey(Semester, default='', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ", " + str(self.semester)
