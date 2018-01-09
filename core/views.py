from django.shortcuts import render


def index(request):
    context = {
        'title': 'django e-commerce'
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'product_list.html')


def product(request):
    return render(request, 'product.html')