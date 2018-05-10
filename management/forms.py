from django import forms
import datetime
from django.forms import ModelForm
from management.models import PropertyListing, State, Country
from localflavor.us.forms import USZipCodeField

class PropertyListingForm(forms.ModelForm):
	address = forms.CharField()
	city = forms.CharField()
	state = forms.ModelChoiceField(queryset=State.objects.all())
	zip_code = USZipCodeField()
	beds = forms.IntegerField()
	baths = forms.FloatField()
	
	class Meta:
		model = PropertyListing
		fields = '__all__'
		widgets = {
			'available_date': forms.DateInput(attrs={'class': 'datepicker'})
		}

