from django.test import TestCase, Client #simula o browser
from django.urls import reverse
from model_mommy import mommy
from catalog.models import Product, Category

class ProductListTestCase(TestCase):

   def setUp(self):
      self.url = reverse('product_list')
      self.client = Client()
      mommy.make('catalog.Product', _quantity=10) #ira gerar 10 objetos Produtos
   
   def tearDown(self):
      Product.objects.all().delete()
   
   def test_view_ok(self):
      response = self.client.get(self.url)
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response, 'catalog/product_list.html')
   
   def test_context(self):
      response = self.client.get(self.url)
      self.assertTrue('product_list' in response.context) #verifica se product_list está no context
      product_list = response.context['product_list'] #pega os objetos (QuerySet) gerados em setUp()
      self.assertEquals(product_list.count(), 3) #verifica se tem 3 objetos Product (estamos usando paginacao)
   
   def test_page_not_found(self):
      """Verifica se retorna 404 ao acessar uma página inexistente"""
      response = self.client.get('{}?page=20'.format(self.url))
      self.assertEquals(response.status_code, 404)
   
