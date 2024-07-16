
from django.urls import path
from jogo import views

urlpatterns = [
    # usuario.com
    path("", views.home, name="home"),
    path("jogo/", views.usuarios, name="game")
]
