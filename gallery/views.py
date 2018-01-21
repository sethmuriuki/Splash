from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Gallery

# Create your views here.
def images(request):
    picture = Gallery.objects.all()
    return render(request, 'index.html', {'picture':picture})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_galleries = Gallery.search_by_tags(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"galleries": searched_galleries})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})