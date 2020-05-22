from django.db import models

class Student(models.Model):

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    edu = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)

class Meta:
    db_table = 'student'


