from django.urls import path 
from . import views

urlpatterns = [
    path("", views.webpage1, name='webpage1'),
    path("about_us/", views.webpage2, name='webpage2'),
    path("admin/", views.webpage3, name='webpage3'),
    path("buy/", views.webpage4, name='webpage4'),
    path("index/", views.webpage5, name='webpage5'),
    path("login/", views.webpage6, name='webpage6'),
    path("menclothing/", views.webpage7, name='webpage7'),
    path("menshoes/", views.webpage8, name='webpage8'),
    path("menswimware/", views.webpage9, name='webpage9'),
    path("register/", views.webpage10, name='webpage10'),
    path("womenclothing/", views.webpage11, name='webpage11'),
    path("womenshoes/", views.webpage12, name='webpage12'),
    path("womenswimware/", views.webpage13, name='webpage13'),
    ]