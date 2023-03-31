from django.contrib import admin

# Register your models here.
from . models import Place
admin.site.register(Place)
from . models import people
admin.site.register(people)
from . models import picture
admin.site.register(picture)