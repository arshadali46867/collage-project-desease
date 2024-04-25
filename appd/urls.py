from django.urls import path 
from . import views 

urlpatterns = [ 
	path("diabetes", views.home), 
    path("predict", views.predict), 
    path("result", views.result),
] 
