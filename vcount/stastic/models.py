from django.db import models

class Payment(models.Model):
    count = models.PositiveIntegerField()
    datetime = models.DateTimeField()