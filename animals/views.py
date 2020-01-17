from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Animal


class CreateAnimal(CreateView):
    template_name = "createanimal.html"
    model = Animal
    fields = [
        'profile_picture',
        'animal_type',
        'color',
        'breed',
        'age',
        'euth_date',
        'id_number',
        'current_pledges',
        'goal',
        'neutered_spayed',
        'current_shelter',
        'name',
        'description',
        'hw',
        'surrender_reason',
        'weight',
    ]
    success_url = 'listanimals/'


class ListAnimals(ListView):
    template_name = "fullanimallist.html"
    model = Animal
    context_object_name = "animals"
    fields = [
        'profile_picture',
        'name',
        'id_number',
        'current_pledges',
        'goal',
        'animal_type',
        'current_shelter',
        'breed',
        'color',
        'name',
    ]
