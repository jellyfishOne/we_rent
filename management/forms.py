from django import forms
import datetime
from django.contrib.admin import widgets
from management.models import PropertyListing, State, Country

class PropertyListingForm(forms.ModelForm):
	address = forms.CharField()
	city = forms.CharField()
	state = forms.ModelChoiceField(queryset=State.objects.all())
	zip_code = forms.CharField(max_length=12)
	beds = forms.IntegerField()
	baths = forms.FloatField()
	available_date = forms.DateField(widget=widgets.AdminDateWidget)
	class Meta:
		model = PropertyListing
		fields = '__all__'