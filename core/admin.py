from django.contrib import admin
from animals.models import *
from shelters.models import *
from authentication.models import *
from core.models import *

# Register your models here.
admin.site.register(Animal)
admin.site.register(Shelter)
admin.site.register(Profile)
