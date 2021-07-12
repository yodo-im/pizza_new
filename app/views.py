from .models import Category, Product
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,  'app/index.html', {
                            'categories': categories,
                            'products': products,
                  })


