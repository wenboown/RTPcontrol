from django.db import models
import datetime

# Create your models here.
class Recipe(models.Model):
    step = models.IntegerField()
    ramp_time = models.IntegerField()
    soak_level = models.FloatField()
    soak_time = models.IntegerField()
    class Meta:
        ordering = ["step"]
        app_label = 'Tcontrol'


class Logs(models.Model):
    time_stamp = models.DateTimeField(default = datetime.datetime.today())
    user = models.CharField(max_length=128)
    class Meta:
        app_label = 'Tcontrol'

