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
      