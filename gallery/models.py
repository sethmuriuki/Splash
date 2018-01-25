from django.db import models

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    tags = models.ManyToManyField(tags)
    category = models.ManyToManyField(categories)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_tags(cls,search_term):
        gallery = cls.object.filter(tags__icontains=search_term)

        return gallery