from django.shortcuts import render,redirect
from django.http import HttpRequest
from app.models import Category
from app.forms import CategoryForm

# Create your views here.

def home(request):
    return render(request,'app/home/home.html')

def category_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/categories/index.html',
        {
            'categories': Category.objects.all()
        }
    )