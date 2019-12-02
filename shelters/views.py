from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Shelter

class CreateShelter(CreateView):
    template_name = "createview.html"
    model = Shelter
    fields = [
        'shelter_name',
        'address',
        'phone',
        'email',
        'website']
    success_url = 'list_inventory'

class ListShelters(ListView):
    template_name = "listview.html"
    model = Shelter
