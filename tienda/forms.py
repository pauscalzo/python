from django import forms
from .models import Producto, Categoria, Marca

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'marca', 'imagen']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
