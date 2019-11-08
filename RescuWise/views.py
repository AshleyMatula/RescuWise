from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.models import Animal

class AnimalIndex(ListView):
    model = Animal
    template_name = 'animals.html'

class Home(TemplateView):
    template_name = "index.html"

class DynamicStaticPages(TemplateView):


    def get_template_names(self, **kwargs):
    
        if self.kwargs.get('template_name'):
            # favicons load first so with out this this dynamic view doesn't work.
            if self.kwargs.get('template_name') == "favicon.ico":
                pass
            else:
                return self.kwargs.get('template_name')
        #if there is no url default it index.html

        return "index.html"
