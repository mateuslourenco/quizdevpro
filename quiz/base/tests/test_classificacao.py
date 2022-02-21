import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('classificacao'))


def test_status_code(resp):
    assert resp.status_code == 302
    assert resp.url == reverse('home')
#
#
# @pytest.fixture
# def resp_com_aluno_logado(client_com_aluno_logado, aluno, pergunta):
#     return client_com_aluno_logado.get(reverse('classificacao'))
#
#
# def test_status_code_aluno_logado(resp_com_aluno_logado):
#     assert resp_com_aluno_logado.status_code == 200
