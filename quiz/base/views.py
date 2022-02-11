from django.shortcuts import render, redirect

from quiz.base.forms import AlunoForm
from quiz.base.models import Pergunta, Aluno


def home(request):
    if request.method == 'POST':
        # Usuário já existe
        email = request.POST['email']
        try:
            aluno = Aluno.objects.get(email=email)
        except Aluno.DoesNotExist:
            # Usuário não existe
            formulario = AlunoForm(request.POST)
            if formulario.is_valid():
                aluno = formulario.save()
                request.session['aluno_id'] = aluno.id
                return redirect('/perguntas/1')
            else:
                ctx = {'formulario': formulario}
                return render(request, 'base/home.html', context=ctx)
        else:
            request.session['aluno_id'] = aluno.id
            return redirect('/perguntas/1')
    return render(request, 'base/home.html')


def classificacao(request):
    return render(request, 'base/classificacao.html')


def perguntas(request, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    ctx = {'indice_da_questao': indice, 'pergunta': pergunta}
    return render(request, 'base/game.html', context=ctx)
