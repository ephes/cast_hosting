from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, url, path, re_path
from django.views.generic import TemplateView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from apps.views import test_site

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("site/", test_site, name="test-site"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Threadedcomments
    re_path(r"^show/comments/", include("fluent_comments.urls")),
    # Wagtail
    url(r"^cms/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"", include(wagtail_urls)),  # default is wagtail
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
