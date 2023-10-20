from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100 ,unique=True)
    description = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to='categories/imgs/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.name}"
    
    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()
    
    def get_image_url(self):
        return f"/media/{self.img}"
    
    def get_profile_url(self):
        return reverse('categories.profile', args=[self.id])