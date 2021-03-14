from django.db import models

# Create your models here.
class MyTaskList (models.Model):
    taskList = models.CharField(max_length = 50)

    def __str__(self):
        return self.taskList