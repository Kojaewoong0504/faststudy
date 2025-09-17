from fastapi import APIRouter, HTTPException, status
from typing import List
from odmantic import ObjectId
from backend.src.models.tutorial import Tutorial
from backend.src.services.tutorial_service import tutorial_service
from pydantic import BaseModel

router = APIRouter()

class TutorialCreate(BaseModel):
    title: str
    category_id: ObjectId
    content: str
    order: int

class TutorialUpdate(BaseModel):
    title: str = None
    category_id: ObjectId = None
    content: str = None
    order: int = None

@router.get("/categories/{category_id}/tutorials", response_model=List[Tutorial])
async def get_tutorials_by_category(category_id: ObjectId):
    tutorials = await tutorial_service.get_tutorials_by_category(category_id)
    return tutorials

@router.get("/tutorials/{tutorial_id}", response_model=Tutorial)
async def get_tutorial_by_id(tutorial_id: ObjectId):
    tutorial = await tutorial_service.get_tutorial_by_id(tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorial not found")
    return tutorial

@router.post("/tutorials", response_model=Tutorial, status_code=status.HTTP_201_CREATED)
async def create_tutorial(tutorial: TutorialCreate):
    created_tutorial = await tutorial_service.create_tutorial(
        title=tutorial.title,
        category_id=tutorial.category_id,
        content=tutorial.content,
        order=tutorial.order
    )
    if not created_tutorial:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category not found or invalid data")
    return created_tutorial

@router.put("/tutorials/{tutorial_id}", response_model=Tutorial)
async def update_tutorial(tutorial_id: ObjectId, tutorial: TutorialUpdate):
    updated_tutorial = await tutorial_service.update_tutorial(
        tutorial_id=tutorial_id,
        title=tutorial.title,
        category_id=tutorial.category_id,
        content=tutorial.content,
        order=tutorial.order
    )
    if not updated_tutorial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorial not found or invalid category")
    return updated_tutorial

@router.delete("/tutorials/{tutorial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tutorial(tutorial_id: ObjectId):
    if not await tutorial_service.delete_tutorial(tutorial_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorial not found")
    return