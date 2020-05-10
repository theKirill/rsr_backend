from django.db import models

# Create your models here.
class RoadSignType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

class RoadSign(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(RoadSignType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    important_info = models.CharField(max_length=500)