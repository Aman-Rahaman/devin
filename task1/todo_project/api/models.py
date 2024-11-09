from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task