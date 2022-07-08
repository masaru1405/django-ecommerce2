
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('catalogo/', include('catalog.urls')),
    path('account/', include('account.urls')),
]
