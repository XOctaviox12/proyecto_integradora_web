from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("creadores/", views.creators, name="creators"),
    path("contacto/", views.contact, name="contact"),
    path("registro/", views.registro, name="registro"),  # 👈 nuevo
]
