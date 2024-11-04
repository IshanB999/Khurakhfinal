from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'
    OTHERS = 'others'


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    height_feet = models.PositiveIntegerField("Height (feet)", blank=True, null=True)
    height_inches = models.PositiveIntegerField("Height (inches)", blank=True, null=True)
    gender = models.CharField(max_length=10,choices=Gender.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Mood(models.TextChoices):
    HAPPY = 'happy'
    NETURAL = 'netural'
    SAD = 'sad'

class ProgressReport(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    weight_kg = models.DecimalField("Weight (kg)", max_digits=5, decimal_places=2)
    mood = models.CharField(max_length=20,choices=Mood.choices)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
