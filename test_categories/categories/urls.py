from django.urls import path
from django.contrib import admin
from . import views
from .models import Product 
#from django.conf.urls import url
from django_filters.views import object_filter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.category),
]

