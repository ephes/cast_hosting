from django.shortcuts import render


def test_site(request):
    return render(request, "pages/site.html")
