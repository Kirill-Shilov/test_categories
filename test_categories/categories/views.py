from django.shortcuts import render
#from filters import ProductFilter
from .models import Category, Product
from .filters import ProductFilter, get_queryset_descendants


def index(request):
    qs = Category.objects.all()
    return render(request, 'categories/tree_template.html', {
        'category_tree': qs,
        })


def category(request, slug):
    current_category = Category.objects.get(slug=slug).get_descendants(include_self=False)
    qs = get_queryset_descendants(current_category)
    f = ProductFilter(request.GET, queryset=Product.objects.filter(category=current_category))
    return render(request, 'categories/category.html', {
        'category_tree': qs,
        'filter': f
        })
