from django.urls import path, URLPattern
from .views import *

urlpatterns = [
    path('wetsuits/', WetsuitsView.as_view()),
    path('wetsuits/<str:category>/', WetsuitsByCategoryView.as_view())

]
