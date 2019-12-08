from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from .models import Product
from carts.models import Cart
# Create your views here.

class Productlistview(ListView):
    queryset = Product.objects.all()
    template_name = "product/products_list.html"
    #how to get dat from the database to our class base views
    def get_context_data(self, *args, **kwargs):
        context = super(Productlistview,self).get_context_data(*args, **kwargs)
        return context

class Productdetailview(DetailView):
    queryset = Product.objects.all()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productdetailview,self).get_context_data(*args, **kwargs)
        return context

class Productslugdetailview(DetailView):
    queryset = Product.objects.all()
    template_name = "product/Productfeatured_detail.html"
    def get_context_data(self, *args,**kwargs):
        context=super(Productslugdetailview,self).get_context_data(*args,**kwargs)
        request = self.request
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request=self.request)
            context['cart'] = cart_obj
        return context

# class for catagory vice
class Productfeaturedlistview(ListView):#exotic
    template_name = "product/item_list.html"
    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()
class Productcat(ListView):
    template_name = "product/item_list.html"
    def get_queryset(self, *args, **kwargs):
        return Product.objects.cat()
class Productdog(ListView):
    template_name = "product/item_list.html"
    def get_queryset(self, *args, **kwargs):
        return Product.objects.dog()
class Productbird(ListView):
    template_name = "product/item_list.html"
    def get_queryset(self, *args, **kwargs):
        return Product.objects.bird()
class Productaccessories(ListView):
    template_name = "product/item_list.html"
    def get_queryset(self, *args, **kwargs):
        return Product.objects.accessories()
class Productfish(ListView):
    template_name = "product/item_list.html"
    def get_queryset(self, *args, **kwargs):
        return Product.objects.fish()

#classes for catagorty
class Productfeaturedslug(DetailView):
    queryset = Product.objects.featured()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productfeaturedslug,self).get_context_data(*args, **kwargs)
        request = self.request
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request=self.request)
            context['cart'] = cart_obj
        return context
class Productcatslug(DetailView):
    queryset = Product.objects.cat()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productcatslug,self).get_context_data(*args, **kwargs)
        request = self.request
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request=self.request)
            context['cart'] = cart_obj
        return context
class Productfishslug(DetailView):
    queryset = Product.objects.fish()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productfishslug,self).get_context_data(*args, **kwargs)
        request = self.request
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request)
            context['cart'] = cart_obj
        return context
class Productdogslug(DetailView):
    queryset = Product.objects.dog()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productdogslug,self).get_context_data(*args, **kwargs)
        request = self.request
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request=self.request)
            context['cart'] = cart_obj
        return context
class Productbirdslug(DetailView):
    queryset = Product.objects.bird()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productbirdslug,self).get_context_data(*args, **kwargs)
        request = self.request
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request=self.request)
            context['cart'] = cart_obj
        return context
class Productaccessoriesslug(DetailView):
    queryset = Product.objects.accessories()
    template_name = "product/products_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(Productaccessoriesslug,self).get_context_data(*args, **kwargs)
        request=self.request
        if request.user.is_authenticated:
            cart_obj,new_obj = Cart.objects.new_or_get(request=self.request)
            context['cart'] = cart_obj
        return context



