import pytest
from django.urls import reverse
from model_mommy import mommy

from quiz.base.models import Aluno


@pytest.fixture
def resp(client):
    return client.get(reverse('home'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def aluno(db):
    aluno_modelo = mommy.make(Aluno)
    return aluno_modelo


@pytest.fixture
def resp_post(client, aluno):
    return client.post(reverse('home'), {'nome': aluno.nome, 'email': aluno.email})


def test_aluno_existente_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == '/perguntas/1'
