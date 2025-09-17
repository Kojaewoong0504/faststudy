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
async def test_get_categories_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # response = await client.get("/categories")
    # assert response.status_code == 200
    # assert isinstance(response.json(), list)
    # if response.json():
    #     category = response.json()[0]
    #     assert "id" in category
    #     assert "name" in category
    #     assert "description" in category
    
    # 현재는 테스트가 실패하도록 더미 값 반환
    assert False, "GET /categories contract test: Implement actual API call"

@pytest.mark.asyncio
async def test_get_category_by_id_contract():
    # TODO: FastAPI 애플리케이션이 준비되면 실제 API 호출로 대체
    # test_category_id = "60d5ec49f8c7a4001c8c4d0a" # 예시 ID, 실제로는 생성된 ID 사용
    # response = await client.get(f"/categories/{test_category_id}")
    # assert response.status_code == 404 # 존재하지 않는 ID이므로 404 예상

    # TODO: 실제 카테고리 생성 후 200 응답 테스트 추가
    # response = await client.post("/categories", json={"name": "Test Category", "description": "Test Description"})
    # created_category_id = response.json()["id"]
    # response = await client.get(f"/categories/{created_category_id}")
    # assert response.status_code == 200
    # assert "id" in response.json()
    # assert "name" in response.json()

    # 현재는 테스트가 실패하도록 더미 값 반환
    assert False, "GET /categories/{category_id} contract test: Implement actual API call"