from django.shortcuts import render
from .models import Product
from .forms import productForm


# HTML form (form only implemented in HTML only)
def product_create_view(request):
    print(request.GET['id'])
    print(request.POST)
    context = {}
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = productForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = productForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj,
    }

    # In App template
    return render(request, "products/product_detail.html", context)

    # From the main Templates folder
    # return render(request,"product/detail.html", context)
