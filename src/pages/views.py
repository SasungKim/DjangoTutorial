from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")


def about_view(request, *args, **kwargs):
    content = {
        "about_text": "Information about our company",
        "about_number": 32,
        "about_list": [111, 225, 363]
    }
    return render(request, "about.html", content)
