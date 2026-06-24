import datetime
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from livro.models import Livros, Categoria, Emprestimo
from usuario.models import Usuarios
from .forms import CadastroLivro, CategoriaLivro
from django.db.models import Q
# Create your views here.


def home(requests):
    if requests.method == "GET":
        if requests.session.get("usuario"):
            status = requests.GET.get("status")
            usuario = Usuarios.objects.get(id=requests.session["usuario"])
            usuarios = Usuarios.objects.all()
            livros = Livros.objects.filter(usuario=usuario)
            livros_all = Livros.objects.filter(
                usuario=requests.session["usuario"]
            ).filter(emprestado=False)
            livros_emprestados = Livros.objects.filter(
                usuario=requests.session["usuario"]
            ).filter(emprestado=True)
            forms = CadastroLivro()
            forms.fields["usuario"].initial = requests.session.get("usuario")
            categoria = Categoria.objects.filter(
                usuario_id=requests.session.get("usuario")
            )
            form_categoria = CategoriaLivro()
            forms.fields["categoria"].queryset = categoria  # type:ignore

            return render(
                requests,
                "home.html",
                {
                    "usuario": usuario,
                    "usuarios": usuarios.exclude(id=requests.session["usuario"]),
                    "livros": livros,
                    "forms": forms,
                    "status": status,
                    "form_categoria": form_categoria,
                    # todos os livros que não estão emprestados
                    "livros_all": livros_all,
                    # todos os livros emprestados
                    "livros_emprestados": livros_emprestados,
                    "total_livro": livros.count(),
                },
            )
        return redirect("/auth/login/?status=2")


def ver_livro(requests, id):
    if requests.session.get("usuario"):
        usuario = Usuarios.objects.get(id=requests.session["usuario"])
        livro = Livros.objects.get(id=id)
        livros = Livros.objects.filter(usuario=usuario)
        emprestimos = Emprestimo.objects.filter(livro=livro)
        if requests.session.get("usuario") == livro.usuario.id:  # type: ignore
            categoria = Categoria.objects.filter(
                usuario_id=requests.session.get("usuario")
            )
            usuarios = Usuarios.objects.all()
            status = requests.GET.get("status")
            forms = CadastroLivro()
            forms.fields["usuario"].initial = requests.session.get("usuario")
            categoria = Categoria.objects.filter(
                usuario_id=requests.session.get("usuario")
            )
            form_categoria = CategoriaLivro()
            forms.fields["categoria"].queryset = categoria  # type:ignore
            livros_emprestados = Livros.objects.filter(
                usuario=requests.session["usuario"]
            ).filter(emprestado=True)

            return render(
                requests,
                "ver_livro.html",
                {
                    "livros": livros,
                    "livro": livro,
                    "usuario": usuario,
                    "categoria": categoria,
                    "emprestimos": emprestimos,
                    "forms": forms,
                    "status": status,
                    "form_categoria": form_categoria,
                    "usuarios": usuarios.exclude(id=requests.session["usuario"]),
                    "livros_emprestados": livros_emprestados,
                    "total_livro": livros.count(),
                },
            )
        else:
            return redirect("/livro/home/?satus=1")
    return redirect("/auth/login/?status=2")


def cadastrar_livro(requests):
    if requests.method == "POST":
        form = CadastroLivro(requests.POST,requests.FILES)
        if form.is_valid:
            form.save()
        else:
            HttpResponse('formulario invalido')
    return redirect("home")


def excluir_livro(requests, id):
    # TODO criar uma forma de quando eliminar mostrar o nome do libro que foi eliminado
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect("/livro/home/?status=1")


def cadastrar_categoria(requests):
    form = CadastroLivro(requests.POST)
    name = form.data["name"]
    descricao = form.data["descricao"]
    usuario = requests.POST.get("usuario")
    print(name, descricao, usuario)
    if int(usuario) == int(requests.session.get("usuario")):

        form = Categoria(name=name, descricao=descricao,
                         usuario_id=usuario).save()
        # TODO: ADICIONAR MENSAGUEM DE CADASTRO COM SUCESSO OU SEM SUCESSO
        return redirect("home")
    else:
        return redirect("/livro/home/?status=3")


def cadastrar_emprestimo(requests):
    if requests.method == "POST":
        select_user: str | None = requests.POST.get("select_user")
        select_book = requests.POST.get("select_book")
        select_user_anonimo: str | None = requests.POST.get(
            "select_user_anonimo")
        print(select_user, select_user_anonimo, select_book)

        if select_user:
            emprestimo = Emprestimo(
                nome_emprestado_id=select_user, livro_id=select_book
            ).save()
        else:
            emprestimo = Emprestimo(
                nome_emprestado_anonimo=select_user_anonimo, livro_id=select_book
            ).save()

            livro = Livros.objects.get(id=select_book)
            livro.emprestado = True
            livro.save()
        return redirect("home")
    else:
        return redirect("home")


def devolver_livro(requests):
    id = requests.POST.get('livro_devolvido')
    livro_devolver = Livros.objects.get(id=id)
    livro_devolver.emprestado = False
    livro_devolver.save()
    devolucao = Emprestimo.objects.get(
        Q(livro=livro_devolver) & Q(data_devolucao=None))
    print(devolucao)
    devolucao.data_devolucao = datetime.datetime.now()
    devolucao.save()
    return redirect('home')


def alterar_livro(requests):
    id_livro = requests.POST.get('id_livro')
    titulo = requests.POST.get('titulo')
    co_autor = requests.POST.get('co_autor')
    autor = requests.POST.get('autor')
    categoria = requests.POST.get('categoria')
    print(categoria)
    update_livro = Livros.objects.get(id=id_livro)
    if update_livro.usuario.id == requests.session['usuario']:  # type: ignore
        update_livro.titulo = titulo
        update_livro.autor = autor
        update_livro.co_autor = co_autor
        update_livro.categoria_id = categoria  # type: ignore
        update_livro.save()
        return redirect(f'/livro/ver_livro/{id_livro}')
    else:
        redirect('/auth/sair')


def meus_emprestimos(requests):
    usuario = Usuarios.objects.get(id=requests.session["usuario"])
    emprestimos = Emprestimo.objects.filter(nome_emprestado=usuario)
    status = requests.GET.get("status")
    usuarios = Usuarios.objects.all()
    livros = Livros.objects.filter(usuario=usuario)
    livros_all = Livros.objects.filter(
        usuario=requests.session["usuario"]
    ).filter(emprestado=False)
    livros_emprestados = Livros.objects.filter(
        usuario=requests.session["usuario"]
    ).filter(emprestado=True)
    forms = CadastroLivro()
    forms.fields["usuario"].initial = requests.session.get("usuario")
    categoria = Categoria.objects.filter(
        usuario_id=requests.session.get("usuario")
    )
    form_categoria = CategoriaLivro()
    forms.fields["categoria"].queryset = categoria  # type:ignore
    return render(requests, 'meus_emprestimos.html', {'usuario': usuario, 'emprestimos': emprestimos,                    "usuario": usuario,
                                                      "usuarios": usuarios.exclude(id=requests.session["usuario"]),
                                                      "livros": livros,
                                                      "forms": forms,
                                                      "status": status,
                                                      "form_categoria": form_categoria,
                                                      # todos os livros que não estão emprestados
                                                      "livros_all": livros_all,
                                                      # todos os livros emprestados
                                                      "livros_emprestados": livros_emprestados,
                                                      "total_livro": livros.count(), })


def avaliar_emprestimo(requests):
    avaliacao = requests .POST.get('avaliacao')
    id = requests .POST.get('id_emp')

    avaliar = Emprestimo.objects.get(id=id)
    if avaliar.livro.usuario.id == requests.session['usuario']:  # type:ignore
        avaliar.avaliacao = avaliacao
        avaliar.save()
        return redirect(f'/livro/ver_livro/{avaliar.livro.id}')  # type:ignore
    else:
        return HttpResponse('esse emprestimo não é seu')
