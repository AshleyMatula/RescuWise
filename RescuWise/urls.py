from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # include core app urls (static/non-auth pages)
    path('', include('core.urls')),

    # include shelters app urls
    path('', include('shelters.urls')),

    # include animals app urls
    path('', include('animals.urls')),

    # include authentication urls
    path('', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
