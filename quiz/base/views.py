from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def perguntas(request, indice):
    ctx = {'indice_da_questao': indice}
    return render(request, 'base/game.html', context=ctx)
