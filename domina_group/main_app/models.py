from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserEdit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, blank=True)
    time = models.TimeField(auto_now_add=False, blank=True)

    def __str__(self):
        return self.subject.name
