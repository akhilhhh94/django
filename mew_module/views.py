from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(req):
    context = {
        "name": "Akhil", 
        "products": Product.objects.all()
    }
    return render(req, 'layout.html', context)
