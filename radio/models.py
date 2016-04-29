from django.db import models
from django.utils import timezone


class Radio(models.Model):
    name = models.CharField(max_length=200)
    sequence = models.PositiveSmallIntegerField(max_length=300)
    description = models.TextField()
