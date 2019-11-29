from django.urls import path
from .views import *

urlpatterns = [
    # action urls
    path('createanimal/', CreateAnimal.as_view()),
    path('listanimals/', ListAnimals.as_view()),
]