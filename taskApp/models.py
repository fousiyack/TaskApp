

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return self.title
