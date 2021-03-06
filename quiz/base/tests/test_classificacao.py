import pytest
from django.db.models import Sum
from django.urls import reverse

from quiz.base.models import Pergunta, Resposta
from quiz.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('classificacao'))


@pytest.fixture
def resp_com_aluno_logado_classificacao(client_com_aluno_logado, pergunta, resposta):
    return client_com_aluno_logado.get(reverse('classificacao'))


def test_status_code(resp):
    assert resp.status_code == 302
    assert resp.url == reverse('home')


def test_status_code_aluno_logado(resp_com_aluno_logado_classificacao):
    assert resp_com_aluno_logado_classificacao.status_code == 200


def test_pergunta_existe_no_db(db, resp_com_aluno_logado_classificacao):
    assert Pergunta.objects.exists()


def test_ranking_presente(resp_com_aluno_logado_classificacao):
    assert_contains(resp_com_aluno_logado_classificacao, '<h3>Ranking')


def test_nome_aluno_presente(resp_com_aluno_logado_classificacao, aluno):
    assert_contains(resp_com_aluno_logado_classificacao, aluno.nome)


def test_soma_de_pontos_presente(resp_com_aluno_logado_classificacao, aluno, resposta):
    pontos_dct = Resposta.objects.filter(aluno_id=aluno.id).aggregate(Sum('pontos'))
    pontos = pontos_dct['pontos__sum']
    assert_contains(resp_com_aluno_logado_classificacao, pontos)
