import pytest
from django.urls import reverse

from quiz.base.models import Aluno, Pergunta
from quiz.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('classificacao'))


def test_status_code(resp):
    assert resp.status_code == 302
    assert resp.url == reverse('home')


@pytest.fixture
def resp_com_aluno_logado(client_com_aluno_logado, pergunta, resposta):
    return client_com_aluno_logado.get(reverse('classificacao'))


def test_status_code_aluno_logado(resp_com_aluno_logado):
    assert resp_com_aluno_logado.status_code == 200


def test_pergunta_existe_no_db(db, resp_com_aluno_logado):
    assert Pergunta.objects.exists()


def test_ranking_presente(resp_com_aluno_logado):
    assert_contains(resp_com_aluno_logado, '<h3>Ranking')
