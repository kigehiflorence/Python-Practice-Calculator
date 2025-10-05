import json
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_add_api(client):
    response = client.post("/calculate", json={"operation": "add", "a": 5, "b": 3})
    assert response.status_code == 200
    assert response.get_json()["result"] == 8
