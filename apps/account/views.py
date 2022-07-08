from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class LoginInterfaceView(LoginView):
   template_name = 'account/login.html'

class LogoutInterfaceView(LogoutView):
   pass

class SignupView(CreateView):
   form_class = UserCreationForm
   template_name = 'account/register.html'
   success_url = '/'

   def get(self, request, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('index')
      return super().get(request, *args, **kwargs)