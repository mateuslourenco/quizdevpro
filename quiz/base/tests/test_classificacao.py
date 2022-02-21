import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('classificacao'))


def test_status_code(resp):
    assert resp.status_code == 302
    assert resp.url == reverse('home')
