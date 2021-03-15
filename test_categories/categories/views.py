from django.shortcuts import render
#from filters import ProductFilter
from .models import Category, Product
from .filters import ProductFilter


def index(request):
    qs = Category.objects.all()
    return render(request, 'categories/tree_template.html', {
        'category_tree': qs,
        })


def category(request, slug):
    # category based on url
    current_category = Category.objects.get(slug=slug)
    # category tree
    qs = current_category.get_descendants(include_self=False)
    # products in child categories include current category
    f = ProductFilter(request.GET, queryset=Product.objects.filter(category__in=current_category.get_descendants(include_self=True)))
    return render(request, 'categories/category.html', {
        'category_tree': qs,
        'filter': f
        })
