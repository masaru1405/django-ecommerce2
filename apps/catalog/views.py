from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category

""" def product_list(request):
   product_list = Product.objects.all()
   context = {'product_list':product_list}
   return render(request, 'catalog/product_list.html', context) """

class ProductListView(ListView):
   model = Product
   template_name = 'catalog/product_list.html'
   context_object_name = 'product_list'
   paginate_by = 3

#Vídeo 33
class CategoryListView(ListView):
   model = Category
   template_name = 'catalog/category.html'

   def get_queryset(self):
      #Retorna os produtos de acordo com a categoria: 
      #1)Do campo slug da tabela Categoria (Product.category__Category.slug=x), busca o slug de acordo com o valor recebido pela URL (como estamos usando kwargs, será um param nomeado e nao ordenado). Como category em Product é uma FK para Category, então o Django saberá fazer essa join. Product.category receberá o ID de Category.
      return Product.objects.filter(category__slug=self.kwargs['slug']) #self.kwargs['nomeParam'], virá através da URL, ex: https://..../slug=algumacoisa
   
   def get_context_data(self, **kwargs):
      context_object_name = super(CategoryListView, self).get_context_data(**kwargs)
      context_object_name['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
      return context_object_name

""" def category(request, slug):
   category = Category.objects.get(slug=slug)
   product_list = Product.objects.filter(category=category)
   context = {
      'current_category':category,
      'product_list':product_list
   }
   return render(request, 'catalog/category.html', context)
 """
def product(request, slug):
   product = Product.objects.get(slug=slug)
   context = {
      'product':product
   }
   return render(request, 'catalog/product.html', context)