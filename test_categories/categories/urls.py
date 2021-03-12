from django.urls import path
from . import views
from .models import Product 
#from django.conf.urls import url
from django_filters.views import object_filter

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.index, {'model':  Product}),
]

