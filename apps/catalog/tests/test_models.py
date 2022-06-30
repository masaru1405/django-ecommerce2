from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from catalog.models import Category, Product

class CategoryTestCase(TestCase):

   def setUp(self):
      self.category = mommy.make('catalog.Category') #nome app.Model ou somente NomeDoModel
   
   def test_get_absolute_url(self):
      self.assertEquals(
         self.category.get_absolute_url(),
         reverse('category', kwargs={'slug':self.category.slug})
      )

class ProductTestCase(TestCase):

   def setUp(self):
      self.product = mommy.make(Product, slug='produto')

   def test_get_absolute_url(self):
      self.assertEquals(
         self.product.get_absolute_url(),
         reverse('product', kwargs={'slug':'produto'})
      )