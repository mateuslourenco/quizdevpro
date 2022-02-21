import pytest
from model_bakery import baker

from quiz.base.models import Aluno, Pergunta, Resposta


@pytest.fixture
def aluno(db):
    aluno = baker.make(Aluno)
    return aluno


@pytest.fixture
def pergunta(db):
    alternativas = ['alternativa1', 'alternativa2', 'alternativa3', 'alternativa4']
    pergunta = baker.make(Pergunta, disponivel=True, alternativas=alternativas)
    return pergunta


@pytest.fixture
def resposta(aluno, pergunta):
    resposta = baker.make(Resposta, aluno=aluno, pergunta=pergunta, pontos=200)
    return resposta


@pytest.fixture
def client_com_aluno_logado(aluno, client):
    session = client.session
    session['aluno_id'] = aluno.id
    session.save()
    return client
