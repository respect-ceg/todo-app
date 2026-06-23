import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_metrics(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "text/plain" in resp.content_type
