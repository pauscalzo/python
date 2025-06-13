from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.crear_producto, name='crear_producto'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('marca/', views.crear_marca, name='crear_marca'),
    path('', views.index, name='index'),
]
