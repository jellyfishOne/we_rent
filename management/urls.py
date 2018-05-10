from django.conf.urls import url
from management import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'property_listing/(?P<property_listing_id>\d+)/$', views.property_listing, name='property_listing'),
	url(r'^property_listings/$', views.property_listings, name='property_listings'),
	url(r'^add_property_listing/$', views.add_property_listing, name='add_property_listing'),
]