from django.db import models

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to = 'galleries/', null = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    category = models.ManyToManyField(categories)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)
    

    @classmethod
    def search_by_tags(cls,search_term):
        gallery = cls.object.filter(tags__icontains=search_term)

        return gallery