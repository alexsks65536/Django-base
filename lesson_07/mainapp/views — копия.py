from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

MENU_LINKS = [
    {'href': 'index', 'active_if': ['index'], 'name': 'домой'},
    {'href': 'products:index', 'active_if': ['products:index', 'products:category'], 'name': 'продукты'},
    {'href': 'contact', 'active_if': ['contact'], 'name': 'контакты'},
]

def index(request):
    products = Product.objects.all()[:4]
    content = {'title': 'Магазин', 'content_block_class': 'slider', 'products': products, 'links': MENU_LINKS}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    if not pk:
        selected_category = ProductCategory.objects.first()
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)

    categories = ProductCategory.objects.all()
    products = Product.objects.filter(category=selected_category)
    content = {'title': 'Каталог', 'content_block_class': 'hero-white', 'selected_category': selected_category,
               'categories': categories, 'products': products, 'links': MENU_LINKS}
    return render(request, "mainapp/products.html", content)


def contact(request):

    return render(
        request,
        "mainapp/contact.html",
        context={
            "menu_links": MENU_LINKS,
        },
    )
