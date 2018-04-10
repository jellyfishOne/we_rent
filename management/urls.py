from django.conf.urls import url
from management import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_property_listing/$', views.add_property_listing, name='add_property_listing'),
]