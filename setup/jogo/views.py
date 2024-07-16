from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, "usuarios/home.html")


def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        return render(request, "usuarios/jogo.html")
    else:
        return render(request, "usuarios/home.html")


def snake_game(request):
    return render(request, 'usuarios/jogo.html')
