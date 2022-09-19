
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("r/<slug:slug>", views.findLink, name="get link")
]
