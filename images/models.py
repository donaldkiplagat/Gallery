from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

class categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Image(models.Model):
    title=models.CharField(max_length=60)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
        
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(categories__icontains=search_term)
        return images
