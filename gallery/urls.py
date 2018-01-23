from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
 url(r'^$', views.images, name='myimages'),
 url(r'^search/',views.search_results, name = 'search_results'),
]