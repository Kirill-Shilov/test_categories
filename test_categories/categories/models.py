from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib import admin


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_all_products(self):
        return Product.objects.filter(category__in=self.get_descendants(include_self=True))


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.IntegerField()

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name




