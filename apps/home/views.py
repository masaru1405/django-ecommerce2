from django.shortcuts import render
from catalog.models import Category

def index(request):
   categories = Category.objects.all()
   #context = {'categories':categories} #vem do context_processors de catalog
   return render(request, 'home/index.html')

def contact(request):
   return render(request, 'home/contact.html')

