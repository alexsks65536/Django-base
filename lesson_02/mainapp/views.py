from django.shortcuts import render

# Create your views here.

menu_links = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

def main(request):

    return render(request, 'mainapp/index.html', context={
        'menu_links': menu_links,
    })


def products(request):

    menu_products = [
        {'href': '#', 'name': 'все'},
        {'href': '#', 'name': 'дом'},
        {'href': '#', 'name': 'офис'},
        {'href': '#', 'name': 'модерн'},
        {'href': '#', 'name': 'классика'},
    ]

    list_products = [
        {'pic_product': '../static/img/product-11.jpg', 'title_product': 'Стул повышенного качества', 'desc_product': 'Не оторваться'},
        {'pic_product': '../static/img/product-21.jpg', 'title_product': 'Удобное кресло', 'desc_product': 'оторваться по полной'},
        {'pic_product': '../static/img/product-31.jpg', 'title_product': 'Стул для игр', 'desc_product': 'Отдохнуть и поспать'},
    ]

    return render(request, 'mainapp/products.html', context={
        'menu_links': menu_links, 'menu_products': menu_products, 'list_products': list_products,
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'menu_links': menu_links,
    })


