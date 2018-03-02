from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Gallery

# Create your views here.
def my_images(request):
    images = Gallery.objects.all()
    return render(request, 'index.html', {'images':images})

def single_photo(request, image_id):
    image = Gallery.objects.get(id=image_id)
    return render(request, 'pic.html', {'image':image})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_picture = Gallery.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_picture})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})