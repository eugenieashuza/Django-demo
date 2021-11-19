from django.shortcuts import render,redirect
from django.http import HttpRequest
from app.models import Category, Product
from app.forms import CategoryForm
from app.forms import ProductForm

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
def category_create(request):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        form = CategoryForm()
        return render(
            request,
            'app/categories/create.html',
            {
                'form': form
            }
        )
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/categories')
    
def category_edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(instance=category)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('/categories')
    
def category_delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('/categories') 

#products
def products_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/produits/index.html',
        {
            'produits': Product.objects.all()
        }
    )
    
def product_create(request):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        form = ProductForm()
        return render(
            request,
            'app/produits/create.html',
            {
                'form': form
            }
        )
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/produits')
    
def product_edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(
            request,
            'app/produits/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/produits')
    
def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/produits') 
    