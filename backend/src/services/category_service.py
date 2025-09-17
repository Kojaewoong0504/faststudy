from typing import List, Optional
from odmantic import ObjectId
from backend.src.core.database import mongodb
from backend.src.models.category import Category

class CategoryService:
    async def get_all_categories(self) -> List[Category]:
        categories = await mongodb.engine.find(Category)
        return categories

    async def get_category_by_id(self, category_id: ObjectId) -> Optional[Category]:
        category = await mongodb.engine.find_one(Category, Category.id == category_id)
        return category

    async def create_category(self, name: str, description: Optional[str] = None) -> Category:
        category = Category(name=name, description=description)
        await mongodb.engine.save(category)
        return category

    async def update_category(self, category_id: ObjectId, name: Optional[str] = None, description: Optional[str] = None) -> Optional[Category]:
        category = await mongodb.engine.find_one(Category, Category.id == category_id)
        if category:
            if name:
                category.name = name
            if description is not None:
                category.description = description
            await mongodb.engine.save(category)
        return category

    async def delete_category(self, category_id: ObjectId) -> bool:
        category = await mongodb.engine.find_one(Category, Category.id == category_id)
        if category:
            await mongodb.engine.delete(category)
            return True
        return False

category_service = CategoryService()
