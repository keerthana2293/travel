from django.shortcuts import render
from . models import Place
from . models import people
from . models import picture
from django.shortcuts import render

from .models import Place
from .models import people
from .models import picture


# Create your views here.
def prg(request):

    obj=Place.objects.all()
    obj1=people.objects.all()
    rkt=picture.objects.all()
    return render(request,"index.html",{'result':obj,
                                        'elemt':obj1,'object': rkt})

