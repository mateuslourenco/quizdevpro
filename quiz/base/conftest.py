import pytest
from model_bakery import baker

from quiz.base.models import Aluno, Pergunta, Resposta


@pytest.fixture
def aluno(db):
    return baker.make(Aluno)


@pytest.fixture
def pergunta(db):
    alternativas = ['alternativa1', 'alternativa2', 'alternativa3', 'alternativa4']
    pergunta = baker.make(Pergunta, disponivel=True, alternativas={'array': alternativas})
    return pergunta


@pytest.fixture
def resposta(aluno, pergunta):
    resposta = baker.make(Resposta, aluno=aluno, pergunta=pergunta, pontos=1000)
    return resposta


@pytest.fixture
def client_com_aluno_logado(aluno, client):
    session = client.session
    session['aluno_id'] = aluno.id
    session.save()
    return client
