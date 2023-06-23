from django.shortcuts import render, HttpResponse
from django.urls import reverse


# Create your views here.


def first_api(request):
    return HttpResponse("Hello this is first api")


def login_page(request):
    url_path = reverse("authentication")
    return render(request, "login_page.html", data=url_path)


def authentication(request):
    data = request.form

    return HttpResponse("Its done")


def index(request):

    return render(request, "AdminLTE-3.2.0/iframe.html")
