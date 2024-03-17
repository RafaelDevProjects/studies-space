from django.shortcuts import render



def index(request):
    dados = {
    1: {"nome": "Nebulososa de Carina", 
        "legenda": "webbbtelecope.com"},

    2: {"nome": "galaxis", 
        "legenda": "nasa.org"}
    }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')

