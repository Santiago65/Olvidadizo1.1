from django.db import models
from django.contrib.auth.models import User

# Create your mocldels here.
class Users(models.Model):
    username = models.CharField(max_length=15)
    passwords = models.CharField(max_length=15)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cumple(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title + ' - by ' + self.user.username
