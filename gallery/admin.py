from django.contrib import admin

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    
admin.site.register(Gallery)
admin.site.register(tags)