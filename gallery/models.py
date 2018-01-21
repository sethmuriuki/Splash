from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    gallery_image = models.ImageField(upload_to = 'gallery/', null = True, blank = True)


class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name