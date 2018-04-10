from django import forms
from management.models import PropertyListing, State, Country

class PropertyListingForm(forms.ModelForm):
	state = forms.CharField()

	class Meta:
		model = PropertyListing
		fields = ('state',)