from django.db import models
from Accounts.models import AccountBase as User

# Create your models here.

class SubTask(models.Model):
   title            = models.CharField(max_length=250)
   description      = models.CharField(max_length=250)
   assigned_to      = models.ManyToManyField(User)
   creation_date    = models.DateField(auto_now=True)
   due_date         = models.DateField(blank=True, null=True)
   
   def __str__(self):
       return self.title



class Task(models.Model):
   task_title       = models.CharField(max_length=250)
   description      = models.CharField(max_length=250)
   assigned_to      = models.ManyToManyField(User)
   creation_date    = models.DateField(auto_now=True)
   due_date         = models.DateField(blank=True, null=True)
   completed        = models.BooleanField(default=False)
   subtasks         = models.ForeignKey(SubTask, on_delete=models.CASCADE)

   def __str__(self):
      return self.task_title
