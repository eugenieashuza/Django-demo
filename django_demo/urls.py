"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#import url 
from django.conf.urls import url
from django.urls import path

#import app.views
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),

    #views
    url(r'^$',app.views.home, name='home'),
    #show categories
    url(r'^categories/$',app.views.category_index, name='category_index'),
    #show add 
    url(r'^categories/create$',app.views.category_create, name='category_create'),
    #edit 
    path('categories/edit/<int:id>', app.views.category_edit, name='category_edit'),
    #delete
    path('categories/delete/<int:id>', app.views.category_delete, name='category_delete'),
    
    #products
    path('produits', app.views.products_index, name='products_index'),
    #show add 
    path('produits/create',app.views.product_create, name='product_create'),
    #edit 
    path('produits/edit/<int:id>', app.views.product_edit, name='product_edit'),
    #delete
    path('produits/delete/<int:id>', app.views.product_delete, name='product_delete'),

     
]
