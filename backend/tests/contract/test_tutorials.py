import pytest
from httpx import AsyncClient

# FastAPI 애플리케이션은 나중에 main.py에서 임포트될 예정
# from backend.src.main import app

# 테스트용 클라이언트 생성 (FastAPI 애플리케이션이 준비되면 사용)
# @pytest.fixture(scope="module")
# async def client():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac

@pytest.mark.asyncio
async def test_get_tutorials_by_category_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # test_category_id = "60d5ec49f8c7a4001c8c4d0a" # 예시 ID, 실제로는 생성된 ID 사용
    # response = await client.get(f"/categories/{test_category_id}/tutorials")
    # assert response.status_code == 200
    # assert isinstance(response.json(), list)

    assert False, "GET /categories/{category_id}/tutorials contract test: Implement actual API call"

@pytest.mark.asyncio
async def test_get_tutorial_by_id_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # test_tutorial_id = "60d5ec49f8c7a4001c8c4d0b" # 예시 ID
    # response = await client.get(f"/tutorials/{test_tutorial_id}")
    # assert response.status_code == 404

    assert False, "GET /tutorials/{tutorial_id} contract test: Implement actual API call"

@pytest.mark.asyncio
async def test_post_tutorial_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # new_tutorial_data = {
    #     "title": "Test Tutorial",
    #     "category_id": "60d5ec49f8c7a4001c8c4d0a",
    #     "content": "# Test Content",
    #     "order": 1
    # }
    # response = await client.post("/tutorials", json=new_tutorial_data)
    # assert response.status_code == 201
    # assert "id" in response.json()

    assert False, "POST /tutorials contract test: Implement actual API call"

@pytest.mark.asyncio
async def test_put_tutorial_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # test_tutorial_id = "60d5ec49f8c7a4001c8c4d0b" # 예시 ID
    # updated_tutorial_data = {
    #     "title": "Updated Tutorial",
    #     "category_id": "60d5ec49f8c7a4001c8c4d0a",
    #     "content": "# Updated Content",
    #     "order": 2
    # }
    # response = await client.put(f"/tutorials/{test_tutorial_id}", json=updated_tutorial_data)
    # assert response.status_code == 200
    # assert response.json()["title"] == "Updated Tutorial"

    assert False, "PUT /tutorials/{tutorial_id} contract test: Implement actual API call"

@pytest.mark.asyncio
async def test_delete_tutorial_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # test_tutorial_id = "60d5ec49f8c7a4001c8c4d0b" # 예시 ID
    # response = await client.delete(f"/tutorials/{test_tutorial_id}")
    # assert response.status_code == 204

    assert False, "DELETE /tutorials/{tutorial_id} contract test: Implement actual API call"