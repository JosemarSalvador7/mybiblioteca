# 📚 mybiblioteca

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0%2B-green)](https://www.djangoproject.com/)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-purple)](https://docs.astral.sh/uv/)

## Sobre o Projeto

O **mybiblioteca** é um sistema web desenvolvido em **Django** para **gerenciamento pessoal de livros**. Ele foi criado para ajudar você a organizar sua coleção particular, mantendo um catálogo digital com todos os detalhes das suas obras favoritas, com segurança e privacidade garantidas através de autenticação por sessão.

### 🎯 Funcionalidades

- **📖 Catálogo Pessoal**
  - Cadastro de livros com título, autor, ISBN, editora e ano
  - Upload de capa para cada livro
  - Visualização da sua coleção completa
  - Busca rápida por título ou autor

- **🔐 Segurança e Autenticação**
  - Sistema de login por sessão (Session-based Authentication)
  - Cada usuário tem sua própria coleção privada
  - Proteção de rotas e dados pessoais
  - Logout seguro

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.12+ com Django 6.0+
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Banco de Dados**: SQLite3 (leve e ideal para uso pessoal)
- **Autenticação**: Sistema de sessão nativo do Django
- **Gerenciador de Pacotes**: UV

## 📁 Estrutura do Projeto
mybiblioteca/
├── core/ # Configurações centrais do Django

├── livro/ # App principal de gerenciamento de livros

│ ├── models.py # Modelo: Livro
│ ├── views.py # Lógica das páginas
│ └── admin.py # Interface administrativa
├── usuario/ # App de autenticação e usuários
│ ├── models.py # Modelo: Usuario (estendido)
│ ├── views.py # Login, Logout, Registro
│ └── forms.py # Formulários de autenticação
├── templates/ # Templates HTML
│ ├── base.html # Template base com Bootstrap 5
│ ├── login.html # Página de login
│ └── registro.html # Página de registro
├── media/ # Arquivos de mídia
│ └── capa_livro/ # Capas dos livros (por usuário)
├── manage.py # Script de gerenciamento
├── db.sqlite3 # Banco de dados (seu catálogo)
├── pyproject.toml # Dependências do projeto
└── uv.lock # Lockfile das dependências

text

## 🔐 Sistema de Autenticação

O mybiblioteca utiliza **autenticação baseada em sessão** do Django, garantindo:

- **Login seguro**: Credenciais verificadas antes do acesso
- **Sessões criptografadas**: Cookies assinados para manter a sessão ativa
- **Isolamento de dados**: Cada usuário vê apenas seus próprios livros
- **Controle de acesso**: Páginas protegidas para usuários não autenticados

### Fluxo de Autenticação
1. Usuário se registra ou faz login
2. Sistema cria uma sessão segura
3. Usuário é redirecionado para seu catálogo pessoal
4. Usuário pode fazer logout a qualquer momento


## 👤 Autor

**Josemar Salvador**
- GitHub: [@JosemarSalvador7](https://github.com/JosemarSalvador7)

---

⭐️ **Organize sua biblioteca pessoal com segurança e estilo!** ⭐️
