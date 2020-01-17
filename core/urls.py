from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # General static views
    path('', Home.as_view(), name='home'),

    path('howitworks/', TemplateView.as_view(
        template_name="howitworks.html"), name='howitworks'),

    path('aboutus/', TemplateView.as_view(
        template_name="about.html"), name='aboutus'),

    path('contact/', TemplateView.as_view(
        template_name="contact.html"), name='contact'),
]
