from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 url(r'^$', views.my_images, name='myimages'),
 url(r'^image/(\d+)', views.single_photo, name = 'myimage'),
 url(r'^search/',views.search_results, name = 'search_results'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)