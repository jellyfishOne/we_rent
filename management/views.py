from django.shortcuts import render
from django.http import HttpResponse
from management.forms import PropertyListingForm

def index(request):
	return render(request, 'management/index.html')



def add_property_listing(request):
	form = PropertyListingForm()

	# A HTTP POST?
	if request.method =='POST':
		form = PropertyListingForm(request.POST)

		# Is form vaid?
		if form.is_valid():
			# Save the new property listing to the database
			form.save(commit=True)
			return index(request)
	return render(request, 'management/add_property_listing.html', {'forms': form})

