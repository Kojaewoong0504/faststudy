from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_categories_contract():
    """Ensures the /api/v1/categories endpoint contract is met."""
    response = client.get("/api/v1/categories")
    
    assert response.status_code == 200
    
    # Validate the structure of the response
    data = response.json()
    assert isinstance(data, list)
    
    # If the list is not empty, validate the schema of the first item
    if data:
        item = data[0]
        assert "id" in item
        assert "name" in item
        assert "description" in item
        assert isinstance(item["id"], str)
        assert isinstance(item["name"], str)
        assert isinstance(item["description"], str)
