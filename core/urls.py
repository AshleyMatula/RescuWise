from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    # General static views
    path('', Home.as_view()),
    #path('<template_name>/', DynamicStaticPages.as_view()),
]
