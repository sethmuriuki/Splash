from django.contrib import admin
from .models import Gallery, categories, tags
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    
admin.site.register(Gallery)
admin.site.register(categories)
admin.site.register(tags)
