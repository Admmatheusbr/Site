from django.shortcuts import render
from utilidades.versoes.fabrica import cria_livro

DADOS = {'DADOS' : [cria_livro() for _ in range(5)]}

def view_home(request):
    dados = {'nome': 'Biblioteca 1'}
    return render(request, 'biblioteca/paginas/home.html', context=dados)

def view_sobre(request):
    dados = {'nome': 'Biblioteca 2'}
    return render(request, 'biblioteca/paginas/sobre.html',context=DADOS)

def view_contato(request):
    dados = {'nome': 'Biblioteca 3'}
    return render(request, 'biblioteca/paginas/contato.html',  context=dados)

def view_livros(request):
    return render(request, 'biblioteca/paginas/livros.html', context=DADOS)

def view_livro(request, id):
    busca = {}
    for item in DADOS['DADOS']:
        if item['sigla'] == id:
            busca = item
            break
    return render(request, 'biblioteca/paginas/livro.html', context=busca)

