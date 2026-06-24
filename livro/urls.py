from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),  # type: ignore
    path("ver_livro/<int:id>", views.ver_livro, name="ver_livro"),
    path("cadastrar_livro/", views.cadastrar_livro, name="cadastrar_livro"),
    path("excluir_livro/<int:id>", views.excluir_livro, name="excluir_livro"),
    path("cadastrar_categoria/", views.cadastrar_categoria, name="cadastrar_categoria"),
    path(
        "cadastrar_emprestimo/", views.cadastrar_emprestimo, name="cadastrar_emprestimo"
    ), 
    path("devolver_livro/", views.devolver_livro, name="devolver_livro"),
    path("alterar_livro/", views.alterar_livro, name="alterar_livro"),#type: ignore
    path("meus_emprestimos/", views.meus_emprestimos, name="meus_emprestimos"),
    path("avaliar_emprestimo/",views.avaliar_emprestimo, name="avaliar_emprestimo")
    
]
