from django.urls import path 
from . import views 

urlpatterns = [ 
	path('heart', views.heart, name="heart"), 
	path('hearthome', views.home, name="home"), 
	path('login', views.login, name="login"), 
	path('logout', views.logout, name="logout"), 
    path('',views.CustomerRegistration.as_view(),name='registration'),
] 
