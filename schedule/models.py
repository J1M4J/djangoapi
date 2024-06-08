from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name