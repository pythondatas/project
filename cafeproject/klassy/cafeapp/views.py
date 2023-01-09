from django.shortcuts import render
from . models import place
from . models import fourimages


# Create your views here.
def function(request):
    obj=place.objects.all()
    ob=fourimages.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})