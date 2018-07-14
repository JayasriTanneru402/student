from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    qualification = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='static/photos')