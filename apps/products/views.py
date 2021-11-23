from django.db import models
from apps.products.models import Product,ProductImage
from apps.products.forms import ProductForm,ProductImageForm
from django.views import generic

class ProductIndexView(generic.ListView):

    queryset = Product.objects.all()
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

class ProductDetailView(generic.DeleteView):

    model = Product
    template_name = 'products/detail.html'

