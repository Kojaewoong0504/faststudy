from fastapi import APIRouter, Depends
from typing import List
from src.models.tutorial import Category
from src.services.tutorial_service import TutorialService

router = APIRouter()

@router.get("/api/v1/categories", response_model=List[Category])
def get_categories(service: TutorialService = Depends(TutorialService)):
    """Endpoint to retrieve all tutorial categories."""
    return service.get_all_categories()
