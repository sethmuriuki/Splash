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

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Gallery(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True, blank = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location = models.ForeignKey(location)
    category = models.ForeignKey(categories)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        gallery = cls.object.filter(title__icontains=search_term)

        return gallery