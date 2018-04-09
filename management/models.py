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

class PropertyListing(models.Model):
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=12)
	beds = models.IntegerField()
	baths = models.FloatField()
	available_date = models.DateField(auto_now=False, auto_now_add=False)

	class Meta:
		verbose_name_plural = 'Property Listings'

	def __str__(self):
		return '%s %s' % (self.address, self.city)
