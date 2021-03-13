from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib import admin
from django.utils.text import slugify


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_all_products(self):
        return Product.objects.filter(category__in=self.get_descendants(include_self=True))


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.IntegerField()

    class Meta:
        verbose_name_plural = 'products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name




