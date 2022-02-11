from django.shortcuts import render, redirect

from quiz.base.forms import AlunoForm
from quiz.base.models import Pergunta, Aluno, Resposta


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


PONTUACAO_MAXIMA = 1000


def perguntas(request, indice):
    try:
        aluno_id = request.session['aluno_id']
    except KeyError:
        return redirect('/')
    else:
        try:
            pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
        except IndexError:
            return redirect('/classificacao')
        else:
            ctx = {'indice_da_questao': indice, 'pergunta': pergunta}
            if request.method == 'POST':
                resposta_indice = int(request.POST['resposta_indice'])
                if resposta_indice == pergunta.alternativa_correta:
                    # Armazenar dados da resposta
                    Resposta(aluno_id=aluno_id, pergunta=pergunta, pontos=PONTUACAO_MAXIMA).save()
                    return redirect(f'/perguntas/{indice+1}')
                else:
                    ctx['resposta_indice'] = resposta_indice
            return render(request, 'base/game.html', context=ctx)