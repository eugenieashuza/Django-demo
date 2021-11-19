from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)    
     
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(unique=True, max_length=50)
    category_id = models.ForeignKey(Category , on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    def __str__(self):
        return self.product_name
    
