from django.contrib import admin

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    
admin.site.register(Editor)
admin.site.register(Articles)
admin.site.register(tags)