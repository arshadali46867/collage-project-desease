from django.urls import path 
from . import views 

urlpatterns = [ 
	path('heart', views.heart, name="heart"), 
	path('hearthome', views.home, name="home"), 
] 
