from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    
    category_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
   
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    # Retorna la url que tiene como atributo name= 'products_by_category' , que se encuentra
    # en urls.py y le pasa como argumento la propiedad slug ejem: http://localhost:8000/computadoras
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
   
    def __str__(self):
        return self.category_name
    
    
