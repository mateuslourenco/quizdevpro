import pytest
from django.urls import reverse


@pytest.fixture
def resp_sem_usuario(client):
    return client.get(reverse('perguntas', kwargs={'indice': 1}))


def test_status_code(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url == reverse('home')
