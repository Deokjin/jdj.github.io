from django.db import models

# Create your models here.

class Board(models.Model):
    writer = models.TextField()
    day = models.DateField()
    content = models.CharField(max_length=20)