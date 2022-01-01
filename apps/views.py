from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site



def test_site(request):
    print("request: ", request)
    current_site = get_current_site(request)
    print("current site: ", current_site)
    context = {"current_site": current_site}
    return render(request, "pages/site.html", context=context)


def hello(request):
    return HttpResponse("Hello Cruel World!")
