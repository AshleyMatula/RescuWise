from django.urls import path
from .views import CreateAnimal, ListAnimals

urlpatterns = [
    # action urls
    path('createanimal/', CreateAnimal.as_view(), name='createanimal'),
    path('listanimals/', ListAnimals.as_view(), name='listanimals'),
]
