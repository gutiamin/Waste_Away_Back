from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')


def getdata(request):
    results = Producto.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)


def productos(request):
    queryset = Producto.objects.all()[:10]
    context = {
        'productos': queryset
    }
    return render(request, 'Producto/productos.html', context)


def platos(request):
    queryset = Plato.objects.all()[:10]
    context = {
        'platos': queryset
    }
    return render(request, 'Plato/platos.html', context)


def restaurantes(request):
    queryset = Restaurante.objects.all()[:10]
    context = {
        'restaurantes': queryset
    }
    return render(request, 'Restaurante/restaurantes.html', context)


def inventarios(request):
    queryset = Inventario.objects.all()[:10]
    context = {
        'inventarios': queryset
    }
    return render(request, 'Inventario/inventarios.html', context)


def productoSearch(request):
    p = request.GET.get('q', '');
    queryset = Producto.objects.filter(nombre__icontains=p)[:10]
    context = {
        'productos': queryset,
        'p': p,
    }
    return render(request, 'Producto/search.html', context)


def productoCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            measurement = form.save()
            measurement.save()
            messages.add_message(request, messages.SUCCESS, 'Producto creado correctamente')
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Producto/producto.html', context)


def inventarioCreate(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            measurement = form.save()
            measurement.save()
            messages.add_message(request, messages.SUCCESS, 'Inventario creado correctamente')
        else:
            print(form.errors)
    else:
        form = InventarioForm()

    context = {
        'form': form,
    }

    return render(request, 'Inventario/inventario.html', context)
