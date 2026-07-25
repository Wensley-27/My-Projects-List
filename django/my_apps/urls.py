from django.contrib import admin
from django.urls import path
from my_apps import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index1_view, name="home"),
]
