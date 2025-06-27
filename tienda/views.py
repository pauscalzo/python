from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Producto
from .forms import ProductoForm, CategoriaForm, MarcaForm

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Producto.objects.filter(
                Q(nombre__icontains=query) |
                Q(categoria__nombre__icontains=query) |
                Q(marca__nombre__icontains=query)
            )
        return Producto.objects.all()

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'
    context_object_name = 'producto'

class ProductoCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_producto.html'
    success_url = reverse_lazy('productos')

class ProductoUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'editar_producto.html'
    success_url = reverse_lazy('productos')

class ProductoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('productos')

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

def about(request):
    return render(request, 'about.html')

@staff_member_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

@staff_member_required
def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_marca')
    else:
        form = MarcaForm()
    return render(request, 'crear_marca.html', {'form': form})






