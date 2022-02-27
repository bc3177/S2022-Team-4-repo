from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    return render(request, "authentication/index.html")


def login_view(request):
    return render(request, "authentication/login.html")


def register_view(request):
    return render(request, "authentication/register.html")
