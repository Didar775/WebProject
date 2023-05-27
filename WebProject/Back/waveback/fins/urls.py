from django.urls import path
from .views import * 


urlpatterns = [
    
    path("fins/", FinsView.as_view()),
    
]
