from django.db import models


class State(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=128, unique=True)

	class Meta:
		verbose_name_plural = 'Countries'

	def __str__(self):
		return self.name
