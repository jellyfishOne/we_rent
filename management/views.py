from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from management.forms import PropertyListingForm
from .models import PropertyListing

def index(request):
	return render(request, 'management/index.html')

def property_listing(request,property_listing_id):
	# Show a single property listing 
	property_listing = PropertyListing.objects.get(id=property_listing_id)
	context = {'property_listing': property_listing}
	return render(request, 'management/property_listing.html', context)

def property_listings(request):
	# Show all property listings
	property_listings = PropertyListing.objects.order_by('available_date')
	context = {'property_listings': property_listings}
	return render(request, 'management/property_listings.html', context)

def add_property_listing(request):
	form = PropertyListingForm()
	# A HTTP POST?
	if request.method =='POST':
		form = PropertyListingForm(request.POST)
		if form.is_valid():
			# Save the new property listing to the database
			# TODO is it saving an instance of property listing?
			form.save(commit=True)
			return index(request)
	return render(request, 'management/add_property_listing.html', {'form': form})

