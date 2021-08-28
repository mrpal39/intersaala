from django.shortcuts import render
from .forms import ProductCreate
from django.contrib.auth.models import User
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
    # form_class=ProductCreate
    template_name = "product.html"
    fields=['name','weight','stock']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Product_list(LoginRequiredMixin,ListView):
    model = Products
    template_name = 'homepage.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'item'
    ordering = ['-name']
    paginate_by = 5
    paginate_orphans = 0

class PostDetailView(DetailView):

    model = Products
    context_object_name='pd'
    template_name='products_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# 

class UserProductList(ListView):
    model = Products
    template_name='userproduct.html'
    context_object_name='userlist'
    paginate_by=-5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Products.objects.filter(user=user).order_by('-create_at')
