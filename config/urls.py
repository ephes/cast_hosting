from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from apps.views import test_site

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("site/", test_site, name="test-site"),
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
]
