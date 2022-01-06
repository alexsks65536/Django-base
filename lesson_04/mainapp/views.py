from django.shortcuts import render
from .models import ProductCategory, Product


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


def products(request):

    products = Product.objects.all()
    productCategory = ProductCategory.objects.all()
    return render(
        request,
        "mainapp/products.html",
        context={
            "menu_links": menu_links,
            "products": products,
            "productCategory": productCategory,
        },
    )


def contact(request):

    return render(
        request,
        "mainapp/contact.html",
        context={
            "menu_links": menu_links,
        },
    )
