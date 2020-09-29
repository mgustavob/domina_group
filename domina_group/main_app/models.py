from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username



class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rate = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, blank=True)
    time = models.TimeField(auto_now_add=False, blank=True)

    def __str__(self):
        return self.subject.name
