from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Animal

class CreateAnimal(CreateView):
    template_name = "createview.html"
    model = Animal
    fields = ['animal_type','name']
    success_url = 'listanimals'

class ListAnimals(ListView):
    template_name = "listview.html"
    model = Animal
    fields = [
        'animal_type',
        'current_shelter',
        'breed',
        'color',
        'name',]