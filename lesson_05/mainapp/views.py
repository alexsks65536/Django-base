from django.shortcuts import render
from django.template.defaultfilters import title

from basketapp.models import Basket
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404

def main(request):
    title = "главная"
    products = Product.objects.all()[:4]
    content = {"title": title, "products": products, "menu_links": menu_links}
    return render(request, "mainapp/index.html", content)


menu_links = [
    {"href": "/", "name": "домой"},
    {"href": "/products", "name": "продукты"},
    {"href": "/contact", "name": "контакты"},
]


def products(request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)

        same_products = Product.objects.all()[3:5]

        content = {
            'title': title,
            'links_menu': links_menu,
            'same_products': same_products
        }

        return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "menu_links": menu_links,
        },
    )

def basket(request, links_menu=None, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

    return render(request, 'mainapp/products_list.html', content)
