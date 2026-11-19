import pytest
from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_accueil_message_par_defaut(client, monkeypatch):
    monkeypatch.delenv("MESSAGE", raising=False)
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert reponse.get_json()["message"] == "Bonjour depuis AKS !"


def test_accueil_message_configurable(client, monkeypatch):
    monkeypatch.setenv("MESSAGE", "Message de test")
    assert client.get("/").get_json()["message"] == "Message de test"


def test_health(client):
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.get_json() == {"status": "ok"}


def test_ready(client):
    assert client.get("/ready").status_code == 200


def test_bissextile(client):
    reponse = client.get("/bissextile/2024")
    assert reponse.status_code == 200
    assert reponse.get_json() == {"annee": 2024, "bissextile": True}
