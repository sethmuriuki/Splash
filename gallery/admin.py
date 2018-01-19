from django.contrib import admin
from .models import Gallery, Tags
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    
admin.site.register(Gallery)
admin.site.register(tags)