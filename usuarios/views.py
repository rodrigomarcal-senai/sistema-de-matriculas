from django.shortcuts import redirect, render
from django.contrib.auth import login

from .forms import CadastrarUsuarioForm, LoginUsuarioForm


def cadastrar_usuario(request):
    if request.method == "POST":
        form = CadastrarUsuarioForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("usuarios:login")
    else:
        form = CadastrarUsuarioForm()

    context = {"form": form}
    return render(request, "usuarios/registro.html", context)


def login_usuario(request):
    if request.method == "POST":
        form = LoginUsuarioForm(data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("cursos:index")
    else:
        form = LoginUsuarioForm()

    context = {"form": form}
    return render(request, "usuarios/login.html", context)
