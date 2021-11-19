from django.db.models import fields
from django.forms import ModelForm
from app.models import Category
from app.models import Product

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'