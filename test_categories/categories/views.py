from django.shortcuts import render
#from filters import ProductFilter
from .models import Category, Product
from .filters import ProductFilter


def index(request):
    qs = Category.objects.all()
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'categories/tree_template.html', {
        'cat_tree': qs,
        'filter': f,
    })
