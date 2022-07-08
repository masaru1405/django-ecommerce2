from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.LoginInterfaceView.as_view(), name='login'),
   path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
   path('signup/', views.SignupView.as_view(), name='signup'),
]

#OBS sobre o login e logout 
#https://stackoverflow.com/questions/51906428/django-cannot-import-login-from-django-contrib-auth-views