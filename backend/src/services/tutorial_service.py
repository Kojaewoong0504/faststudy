from typing import List, Optional
from odmantic import ObjectId
from backend.src.core.database import mongodb
from backend.src.models.tutorial import Tutorial
from backend.src.models.category import Category
from datetime import datetime

class TutorialService:
    async def get_all_tutorials(self) -> List[Tutorial]:
        tutorials = await mongodb.engine.find(Tutorial)
        return tutorials

    async def get_tutorials_by_category(self, category_id: ObjectId) -> List[Tutorial]:
        tutorials = await mongodb.engine.find(Tutorial, Tutorial.category_id == category_id)
        return tutorials

    async def get_tutorial_by_id(self, tutorial_id: ObjectId) -> Optional[Tutorial]:
        tutorial = await mongodb.engine.find_one(Tutorial, Tutorial.id == tutorial_id)
        return tutorial

    async def create_tutorial(self, title: str, category_id: ObjectId, content: str, order: int) -> Optional[Tutorial]:
        # Check if category exists
        category = await mongodb.engine.find_one(Category, Category.id == category_id)
        if not category:
            return None

        tutorial = Tutorial(
            title=title,
            category_id=category_id,
            content=content,
            order=order,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        await mongodb.engine.save(tutorial)
        return tutorial

    async def update_tutorial(self, tutorial_id: ObjectId, title: Optional[str] = None, category_id: Optional[ObjectId] = None, content: Optional[str] = None, order: Optional[int] = None) -> Optional[Tutorial]:
        tutorial = await mongodb.engine.find_one(Tutorial, Tutorial.id == tutorial_id)
        if tutorial:
            if title:
                tutorial.title = title
            if category_id:
                # Check if new category exists
                category = await mongodb.engine.find_one(Category, Category.id == category_id)
                if not category:
                    return None
                tutorial.category_id = category_id
            if content:
                tutorial.content = content
            if order is not None:
                tutorial.order = order
            tutorial.updated_at = datetime.utcnow()
            await mongodb.engine.save(tutorial)
        return tutorial

    async def delete_tutorial(self, tutorial_id: ObjectId) -> bool:
        tutorial = await mongodb.engine.find_one(Tutorial, Tutorial.id == tutorial_id)
        if tutorial:
            await mongodb.engine.delete(tutorial)
            return True
        return False

tutorial_service = TutorialService()