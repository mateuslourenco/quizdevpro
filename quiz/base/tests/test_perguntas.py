import pytest
from django.urls import reverse


@pytest.fixture
def client_com_aluno_logado_perguntas(aluno, client):
    session = client.session
    session['aluno_id'] = aluno.id
    session.save()
    return client


@pytest.fixture
def resp_sem_aluno(client):
    return client.get(reverse('perguntas', kwargs={'indice': 1}))


@pytest.fixture
def resp_com_aluno_logado(client_com_aluno_logado_perguntas, pergunta):
    return client_com_aluno_logado_perguntas.get(reverse('perguntas', kwargs={'indice': 1}))


@pytest.fixture
def resp_indice_pergunta_invalido(client_com_aluno_logado, pergunta):
    return client_com_aluno_logado.get(reverse('perguntas', kwargs={'indice': pergunta.id + 1}))


@pytest.fixture
def resp_post(client_com_aluno_logado, pergunta, resposta):
    return client_com_aluno_logado


def test_status_code_sem_aluno(resp_sem_aluno):
    assert resp_sem_aluno.status_code == 302
    assert resp_sem_aluno.url == reverse('home')


def test_status_code_com_aluno(resp_com_aluno_logado):
    assert resp_com_aluno_logado.status_code == 200


def test_status_code_indice_invalido(resp_indice_pergunta_invalido, pergunta, resposta):
    assert resp_indice_pergunta_invalido.status_code == 302
    assert resp_indice_pergunta_invalido.url == reverse('classificacao')
