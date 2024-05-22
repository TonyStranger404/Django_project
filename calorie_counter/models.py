
from django.db import models

class Calorie(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    activity = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.calories} calories"
