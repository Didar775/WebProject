from django.urls import path
from .views import * 


urlpatterns = [
    
    path("surfboards/", Surfboards.as_view()),
    
]
