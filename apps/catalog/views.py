from django.shortcuts import render
from .models import Product, Category

def product_list(request):
   product_list = Product.objects.all()
   context = {'product_list':product_list}
   return render(request, 'catalog/product_list.html', context)

def category(request, slug):
   category = Category.objects.get(slug=slug)
   #print(category)
   product_list = Product.objects.filter(category=category)
   #print(product_list)
   context = {
      'current_category':category,
      'product_list':product_list
   }
   return render(request, 'catalog/category.html', context)

def product(request, slug):
   product = Product.objects.get(slug=slug)
   context = {
      'product':product
   }
   return render(request, 'catalog/product.html', context)