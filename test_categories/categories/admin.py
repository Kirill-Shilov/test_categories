from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'category', 'a', 'b', 'c')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, MPTTModelAdmin)
