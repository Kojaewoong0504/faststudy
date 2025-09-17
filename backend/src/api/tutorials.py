from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from src.models.tutorial import Tutorial
from src.services.tutorial_service import TutorialService

router = APIRouter()

@router.get("/api/v1/tutorials/{tutorial_id}", response_model=Tutorial)
def get_tutorial(tutorial_id: str, service: TutorialService = Depends(TutorialService)):
    """Endpoint to retrieve a specific tutorial by its ID."""
    tutorial = service.get_tutorial_by_id(tutorial_id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return tutorial
