
from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name
