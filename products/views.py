from django.shortcuts import render
from .forms import ProductCreate
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (

    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Products

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Products
    form_class=ProductCreate
    template_name = "product.html"
    
    def form_valid(self, form):
        form.instance.Products = self.request.user
        return super().form_valid(form)

class Product_list(LoginRequiredMixin,ListView):
    model = Products
    template_name = 'homepage.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'prod'
    ordering = ['-name']
    paginate_by = 5
    paginate_orphans = 0

