from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Todo(models.Model):
    completed = models.BooleanField(default=False)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(default=timezone.now)

    def toggle_complete(self):
        if self.completed == True:
            self.completed = False
            #self.completed_date = ''
        else:
            self.completed = True
            self.completed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
