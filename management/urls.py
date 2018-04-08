from django.conf.urls import url
from management import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]