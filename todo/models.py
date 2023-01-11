from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200, blank=True, null=True)
    task_description = models.CharField(max_length=600, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    complete = models.BooleanField(default=False)
    second_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.task_title}"
# Create your models here.
