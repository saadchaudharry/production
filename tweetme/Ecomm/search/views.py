from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q
from tags.models import Tag

# Create your views here.

class Searchview(ListView):
    template_name = "product/products_list.html"

    def get_queryset(self):
        request=self.request
        query=request.GET.get("q")
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.none()