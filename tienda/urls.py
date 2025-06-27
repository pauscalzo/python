from django.urls import path
from .views import (
    index, about,
    ProductoListView, ProductoDetailView,
    ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    crear_categoria, crear_marca,
)

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

    path('productos/', ProductoListView.as_view(), name='productos'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('productos/crear/', ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar_producto'),

    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('crear_marca/', crear_marca, name='crear_marca'),
]

