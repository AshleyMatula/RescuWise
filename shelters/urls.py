from django.urls import path
from .views import *

urlpatterns = [
    # action urls
    path('createshelter/',CreateShelter.as_view()),
    path('listshelters/',ListShelters.as_view()),
]