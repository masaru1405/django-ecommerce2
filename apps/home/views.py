from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from catalog.models import Category
from .forms import ContactForm

def index(request):
   categories = Category.objects.all()
   #context = {'categories':categories} # já tá vindo do context_processors de catalog
   context = {'nome':'PEDRO'}
   return render(request, 'home/index.html', context)

def contact(request):
   success = False
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         name = form.cleaned_data['name']
         email = form.cleaned_data['email']
         message = form.cleaned_data['message']
         message = 'Nome: {}\nEmail: {}\n{}'.format(name, email, message)
         send_mail(
            'Contato do Django Ecommerce', message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL]
         )
         success = True
   else:
      form = ContactForm()
   context = {
      'form':form,
      'success':success
   }
   return render(request, 'home/contact.html', context)

