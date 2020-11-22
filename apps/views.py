from django.shortcuts import render
from django.http import HttpResponse


def test_site(request):
    return render(request, "pages/site.html")


def hello(request):
    return HttpResponse("Hello World!")
