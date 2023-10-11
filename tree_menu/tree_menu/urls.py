from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("menu/", include("menu.urls", namespace="menu")),
    path("admin/", admin.site.urls),
]
