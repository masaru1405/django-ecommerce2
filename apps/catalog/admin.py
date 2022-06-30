from django.contrib import admin
from .models import Product, Category

#admin.site.register([Product, Category])

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug', 'created', 'modified']
   search_fields = ['name', 'slug']

class ProductAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug', 'category', 'created', 'modified']
   search_fields = ['name', 'slug', 'category__name'] #category__nomAtributo, obs que category é uma FK de Category
   list_filter = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
