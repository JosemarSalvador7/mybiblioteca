from hashlib import sha256
from django.shortcuts import render, redirect
from .models import Usuarios


def login(requests):
    if requests.session.get("usuario"):
        return redirect("/livro/home")
    status = requests.GET.get("status")
    return render(requests, "login.html", {"status": status})


def sair(requests):
    requests.session.flush()
    return redirect("login")


def cadastro(requests):
    if requests.session.get("usuario"):
        return redirect("/livro/home")
    status = requests.GET.get("status")
    return render(requests, "cadastro.html", {"status": status})


def valida_cadastro(requests):
    name = requests.POST.get("name")
    password = requests.POST.get("password")
    email = requests.POST.get("email")

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect("/auth/cadastro/?status=1")
    if len(password.strip()) < 8:
        return redirect("/auth/cadastro/?status=2")
    if Usuarios.objects.filter(email=email).exists():
        return redirect("/auth/cadastro/?status=3")

    password = sha256(password.encode()).hexdigest()
    try:
        Usuarios.objects.get_or_create(name=name, password=password, email=email)
        return redirect("/auth/cadastro/?status=0")
    except:
        return redirect("/auth/cadastro/?status=4")


def valida_login(requests):
    email = requests.POST.get("email")
    password = requests.POST.get("password")

    password = sha256(password.encode()).hexdigest()
    user = Usuarios.objects.filter(email=email).filter(password=password)
    if len(user) == 0:
        return redirect("/auth/login/?status=1")
    if len(user) > 0:
        requests.session["usuario"] = user[0].id  # type: ignore
        return redirect("/livro/home")
