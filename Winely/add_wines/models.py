from django.db import models

# Create your models here.
class Wine(models.Model):
	name = models.CharField(max_length=500)
	year = models.IntegerField(default=2010)
	grape = models.CharField(max_length=500)
	producer = models.CharField(max_length=500)
	