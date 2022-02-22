import pytest
from django.urls import reverse

from quiz.django_assertions import assert_contains


@pytest.fixture
def client_com_aluno_logado(aluno, client):
    session = client.session
    session['aluno_id'] = aluno.id
    session.save()
    return client


@pytest.fixture
def resp_sem_aluno(client):
    return client.get(reverse('perguntas', kwargs={'indice': 1}))


@pytest.fixture
def resp_com_aluno_logado(client_com_aluno_logado, pergunta):
    return client_com_aluno_logado.get(reverse('perguntas', kwargs={'indice': 1}))


@pytest.fixture
def resp_indice_perguntas_finalizado(client_com_aluno_logado, pergunta):
    return client_com_aluno_logado.get(reverse('perguntas', kwargs={'indice': pergunta.id + 1}))


def test_status_code_sem_aluno(resp_sem_aluno):
    assert resp_sem_aluno.status_code == 302
    assert resp_sem_aluno.url == reverse('home')


def test_status_code_com_aluno(resp_com_aluno_logado):
    assert resp_com_aluno_logado.status_code == 200


def test_status_code_redirect_classificacao(resp_indice_perguntas_finalizado, pergunta, resposta):
    assert resp_indice_perguntas_finalizado.status_code == 302
    assert resp_indice_perguntas_finalizado.url == reverse('classificacao')


def test_id_da_pergunta_presente(resp_com_aluno_logado, pergunta):
    assert_contains(resp_com_aluno_logado, pergunta.id)


def test_enunciado_presente(resp_com_aluno_logado, pergunta):
    assert_contains(resp_com_aluno_logado, pergunta.enunciado)


def test_alternativas_presentes(resp_com_aluno_logado, pergunta):
    for alternativa in pergunta.alternativas['array']:
        assert_contains(resp_com_aluno_logado, alternativa)

