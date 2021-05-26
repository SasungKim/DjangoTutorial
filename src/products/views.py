from django.shortcuts import render
from .models import Product
from .forms import productForm, RawProductForm


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "products/product_create.html", context)

    # # HTML form (form only implemented in HTML only)
    # def product_create_view(request):
    #     if request.method == "POST":
    #         title = request.POST.get('title')
    #         Product.objects.create(title=title)
    #     context = {}
    #     return render(request, "products/product_create.html", context)

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
