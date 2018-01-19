from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.name


    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    @classmethod
    def display_tags(cls):
        all_tags = cls.objects.all()
        return all_tags

    @classmethod
    def search_for_tag(cls,search_term):
        tags = cls.objects.filter(name__icontains=search_term)
        return tags

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    gallery_image = models.ImageField(upload_to = 'gallery/', null = True, blank = True)