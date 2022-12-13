from django.shortcuts import render
from .models import Category, Product
from django.http import Http404
from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404

def shop(request):
    return render(request, 'base.html', {"contents": Product.objects.all(), "categories":Category.objects.all()})

def product_list(request, category_slug=None):
    category=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html',
{
    'category':category,
    'categories': categories,
    'products':products,
})

def detail_product(request, detail):
    try:
        post = Product.objects.get(id=detail)
        return render(request, 'product/detail.html', {"product": post})
    except Product.DoesNotExist:
        raise Http404


def category_slug(request, category_slug):
    for categorys in Category.objects.all():
        if str(category_slug) == str(categorys.slug):
            return render(request, 'base.html', {"contents": Product.objects.filter(category_id=categorys.id), "categories":Category.objects.all()})
        

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

    