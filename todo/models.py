# todo/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)   
    completed = models.BooleanField(default=False)  
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    
    def __str__(self):
        return self.name

