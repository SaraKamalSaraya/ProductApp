from django.db import models
from django.shortcuts import reverse
from categories.models import Categories

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='amazon/imgs/', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    instock = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Categories,null=True,blank=True,on_delete=models.CASCADE,related_name='products')
    owner = models.CharField(max_length=100, default='none')

    def __str__(self):
        return f"{self.name}"
    
    def get_profile_url(self):
        return reverse('amazon.profile', args=[self.id])
    
    def get_delete_url(self):
        return reverse('amazon.delete', args=[self.id])

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    
    def get_image_url(self):
        return f"/media/{self.img}"
    
    @classmethod
    def get_sepcific_object(cls, id):
        return  cls.objects.get(id=id)
    
    def get_edit_url(self):
        return reverse('amazon.edit', args=[self.id])


