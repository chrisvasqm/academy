from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

class Academy(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    
    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    price_per_credit = models.DecimalField(max_digits=6, decimal_places=2)
    academy = models.ForeignKey(Academy, on_delete=CASCADE, related_name='academies')
    
    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
class Enrollment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=PROTECT, related_name='subjects')
    student = models.ForeignKey(Student, on_delete=PROTECT, related_name='students')