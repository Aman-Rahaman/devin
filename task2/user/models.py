from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, default="DEFAULT_USERNAME")
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    REQUIRED_FIELDS = []



#task1
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task
