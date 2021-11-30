from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

class Academy(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField()

class Subject(models.Model):
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    price_per_credit = models.DecimalField(max_digits=6, decimal_places=2)
    academy = models.ForeignKey(Academy, on_delete=CASCADE, related_name='academies')
    
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    
class Enrollment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=PROTECT, related_name='subjects')
    student = models.ForeignKey(Student, on_delete=PROTECT, related_name='students')