from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    section = models.TextField()
    rollno = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    CNIC = models.TextField()


