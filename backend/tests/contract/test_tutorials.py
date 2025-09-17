from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_tutorial_by_id_contract():
    """Ensures the /api/v1/tutorials/{tutorial_id} endpoint contract is met for a valid ID."""
    # We assume a tutorial with id 'class-based-services' will exist.
    tutorial_id = "class-based-services"
    response = client.get(f"/api/v1/tutorials/{tutorial_id}")
    
    assert response.status_code == 200
    
    # Validate the structure of the response
    item = response.json()
    assert "id" in item
    assert "category_id" in item
    assert "title" in item
    assert "content" in item
    assert item["id"] == tutorial_id
    assert isinstance(item["category_id"], str)
    assert isinstance(item["title"], str)
    assert isinstance(item["content"], str)

def test_get_tutorial_not_found_contract():
    """Ensures the endpoint returns 404 for a non-existent tutorial ID."""
    tutorial_id = "non-existent-id"
    response = client.get(f"/api/v1/tutorials/{tutorial_id}")
    
    assert response.status_code == 404
