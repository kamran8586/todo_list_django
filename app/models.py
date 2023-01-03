from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
