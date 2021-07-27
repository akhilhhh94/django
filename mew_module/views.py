from django import forms
from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect
from .models import Product
from .forms import SubscriptionForm

# Create your views here.
def index(req):
    if req.method == 'POST':
        form = SubscriptionForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = SubscriptionForm() # An unbound form
    context = {
        "name": "Akhil", 
        "products": Product.objects.all(),
        "form": SubscriptionForm
    }

    return render(req, 'layout.html', context)
