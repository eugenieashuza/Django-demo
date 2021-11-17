from django.db import models
#class categorie
class categorie(models.Model):
    category_name = models.CharField(unique=True, max_length=50)    

     def __str__(self) ->str :
         return self.category_name