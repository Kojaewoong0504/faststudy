from fastapi import APIRouter, HTTPException, status
from typing import List
from odmantic import ObjectId
from backend.src.models.category import Category
from backend.src.services.category_service import category_service

router = APIRouter()

@router.get("/categories", response_model=List[Category])
async def get_all_categories():
    return await category_service.get_all_categories()

@router.get("/categories/{category_id}", response_model=Category)
async def get_category_by_id(category_id: ObjectId):
    category = await category_service.get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category