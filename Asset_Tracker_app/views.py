from django.shortcuts import render,HttpResponse

# Create your views here.


def first_api(request):

    return HttpResponse("Hello this is first api")
