from tkinter import CASCADE
from unicodedata import name
from django.db import models
from datetime import *
from django.contrib.auth.models import User

# Create your models here.
class UserLevel(models.Model):
    name = models.CharField( max_length= 25 , null=True , blank=True)
    subject = models.CharField( max_length=25 , null=True , blank=True)
    marks = models.CharField(  max_length=25 , null=True , blank=True )
    def __str__(self):
        return self.name

