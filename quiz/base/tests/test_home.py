import pytest
from django.urls import reverse
from model_bakery import baker

from quiz.base.models import Aluno


@pytest.fixture
def resp(client):
    return client.get(reverse('home'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def aluno(db):
    aluno_modelo = baker.make(Aluno)
    return aluno_modelo


@pytest.fixture
def resp_post(client, aluno):
    return client.post(reverse('home'), {'nome': aluno.nome, 'email': aluno.email})


def test_aluno_existente_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == '/perguntas/1'


@pytest.fixture
def resp_post_aluno_inexistente(client):
    return client.post(reverse('home'), {'nome': 'novo', 'email': 'novo@novo.com'})


def test_aluno_novo_redirect(db, resp_post_aluno_inexistente):
    assert resp_post_aluno_inexistente.status_code == 302
    assert resp_post_aluno_inexistente.url == '/perguntas/1'


def test_aluno_novo_existe_no_db(db, resp_post_aluno_inexistente):
    assert Aluno.objects.exists()


@pytest.fixture
def resp_dados_invalido(client):
    return client.post(reverse('home'), {'nome': '', 'email': ''})


def test_aluno_nao_existe_no_db(db, resp_dados_invalido):
    assert not Aluno.objects.exists()
