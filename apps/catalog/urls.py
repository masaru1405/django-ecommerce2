from django.urls import path
from . import views

urlpatterns = [
   path('', views.ProductListView.as_view(), name='product_list'),
   path('<slug:slug>', views.CategoryListView.as_view(), name='category'),
   path('produto/<slug:slug>/', views.product, name='product')
]