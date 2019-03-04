from django.db import models
from django.utils import timezone

# Create your models here.



# username,calories,date

class foodfitnessModel(models.Model):
    username=models.CharField(max_length=200, default="")
    calories=models.IntegerField(default="")
    date=models.DateField(default=timezone.now())
    # userTableForeignKey=models.ForeignKey(User,on_delete=)