from email.policy import default
from tkinter import Widget
from turtle import textinput
from django.db import models

# Create your models here.

class Feedback(models.Model):
    CHOICES = (
        ('AS','Australia'),
        ('CN','Canada'),
        ('US', 'United States'),
        ('RU', 'Russia'),
        ('JP','Japan'),
        ('IN','India'),
        ('CH', 'China'),
    )
    firstname=models.CharField(max_length=50)
    lname = models.CharField(max_length = 150)
    mailid=models.EmailField()
    country=models.CharField(max_length=300, choices=CHOICES)
    feedback=models.TextField(max_length=300)
    thumbnail = models.ImageField(upload_to = "uploads/",default='None')



