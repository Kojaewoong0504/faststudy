from typing import List, Optional, Dict
from src.models.tutorial import Category, Tutorial

# In-memory database for tutorials and categories
_DB: Dict[str, List] = {
    "categories": [
        {
            "id": "project-structure",
            "name": "Project Structure",
            "description": "Learn how to structure your FastAPI projects for scalability and maintainability."
        },
        {
            "id": "advanced-patterns",
            "name": "Advanced Patterns",
            "description": "Explore advanced patterns like dependency injection, class-based services, and more."
        }
    ],
    "tutorials": [
        {
            "id": "class-based-services",
            "category_id": "advanced-patterns",
            "title": "Implementing Class-Based Services",
            "content": "This is the full content for the class-based services tutorial. It explains why and how to use classes for your service layer.",
            "author": "Jane Doe"
        }
    ]
}

class TutorialService:
    """Service layer for handling tutorial and category data."""

    def get_all_categories(self) -> List[Category]:
        """Retrieves all categories from the database."""
        return [Category(**cat) for cat in _DB["categories"]]

    def get_tutorial_by_id(self, tutorial_id: str) -> Optional[Tutorial]:
        """Finds a tutorial by its ID."""
        for tut in _DB["tutorials"]:
            if tut["id"] == tutorial_id:
                return Tutorial(**tut)
        return None
