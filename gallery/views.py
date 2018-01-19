from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Gallery

# Create your views here.
def galleries(request):
    picture = Gallery.objects.all()
    return render(request, 'index.html', {'picture':picture})