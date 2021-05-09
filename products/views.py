from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import *

def index(request):
    return render(request, template_name='index.html')

class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    extra_context = {
        'title': 'Seznam produktů'
    }

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'
    extra_context = {
        'title': 'Detail produktu'
    }

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'measure', 'type', 'price', 'mark', 'akce', 'description', 'img']
    extra_context = {
        'title': 'Přídání produktu',
    }

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'measure', 'type', 'price', 'mark', 'akce', 'description', 'img']
    extra_context = {
        'title': 'Úprava produktu',
    }


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('list')