from django.db import models

# Create your models here.

class Avocado_Price(models.Model):
	average_price = models.FloatField()
	total_volume =	models.FloatField()
	avocado_4046 = models.FloatField()
	avocado_4225 = models.FloatField()
	avocado_4770 = models.FloatField()
	total_bags = models.FloatField()
	small_bags = models.FloatField()
	large_bags = models.FloatField()
	xlarge_bags = models.FloatField()
	avocado_type = models.CharField(max_length=60)
	region = models.CharField(max_length=60)

	def __str__(self):
		return self.region