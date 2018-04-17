from django.db import models


class Semester(models.Model):
    sem_name = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.sem_name


class Student(models.Model):
    name = models.CharField(max_length=40)
    semester = models.ForeignKey(Semester, default='', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ", " + str(self.semester)


class Subject(models.Model):
    name = models.CharField(max_length=40)
    optional = models.NullBooleanField(blank=True, null=True)
    semester = models.ForeignKey(Semester, default='', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ", " + str(self.semester)
