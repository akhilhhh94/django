from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    context = {
        "name": "Akhil"
    }
    return render(req, 'layout.html', context)
