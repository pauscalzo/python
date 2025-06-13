from django.shortcuts import render, redirect
from .forms import ProductoForm, CategoriaForm, MarcaForm
from .models import Producto
from django.db.models import Q

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_marca')
    else:
        form = MarcaForm()
    return render(request, 'crear_marca.html', {'form': form})

def index(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(categoria__nombre__icontains=query) |
            Q(marca__nombre__icontains=query)
        )
    else:
        productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})



