import pytest
from unittest.mock import AsyncMock, MagicMock
from odmantic import ObjectId
from backend.src.models.category import Category
from backend.src.models.tutorial import Tutorial
from backend.src.services.category_service import CategoryService
from backend.src.services.tutorial_service import TutorialService
from datetime import datetime

# Mock MongoDB engine
@pytest.fixture
def mock_engine():
    engine = AsyncMock()
    return engine

@pytest.fixture
def category_service_instance(mock_engine):
    service = CategoryService()
    service.mongodb.engine = mock_engine
    return service

@pytest.fixture
def tutorial_service_instance(mock_engine):
    service = TutorialService()
    service.mongodb.engine = mock_engine
    return service

@pytest.mark.asyncio
async def test_get_all_categories(category_service_instance, mock_engine):
    mock_categories = [
        Category(id=ObjectId(), name="Cat1", description="Desc1"),
        Category(id=ObjectId(), name="Cat2", description="Desc2")
    ]
    mock_engine.find.return_value = mock_categories
    
    categories = await category_service_instance.get_all_categories()
    
    assert len(categories) == 2
    assert categories[0].name == "Cat1"
    mock_engine.find.assert_called_once_with(Category)

@pytest.mark.asyncio
async def test_get_category_by_id(category_service_instance, mock_engine):
    test_id = ObjectId()
    mock_category = Category(id=test_id, name="TestCat", description="TestDesc")
    mock_engine.find_one.return_value = mock_category

    category = await category_service_instance.get_category_by_id(test_id)

    assert category.name == "TestCat"
    mock_engine.find_one.assert_called_once_with(Category, Category.id == test_id)

@pytest.mark.asyncio
async def test_create_category(category_service_instance, mock_engine):
    mock_engine.save.side_effect = lambda x: x # Return the saved object
    
    category = await category_service_instance.create_category("NewCat", "NewDesc")
    
    assert category.name == "NewCat"
    assert category.description == "NewDesc"
    mock_engine.save.assert_called_once()

@pytest.mark.asyncio
async def test_update_category(category_service_instance, mock_engine):
    test_id = ObjectId()
    existing_category = Category(id=test_id, name="OldCat", description="OldDesc")
    mock_engine.find_one.return_value = existing_category
    mock_engine.save.side_effect = lambda x: x

    updated_category = await category_service_instance.update_category(test_id, name="UpdatedCat")

    assert updated_category.name == "UpdatedCat"
    assert updated_category.description == "OldDesc"
    mock_engine.find_one.assert_called_once_with(Category, Category.id == test_id)
    mock_engine.save.assert_called_once()

@pytest.mark.asyncio
async def test_delete_category(category_service_instance, mock_engine):
    test_id = ObjectId()
    existing_category = Category(id=test_id, name="CatToDelete")
    mock_engine.find_one.return_value = existing_category
    mock_engine.delete.return_value = None

    result = await category_service_instance.delete_category(test_id)

    assert result is True
    mock_engine.find_one.assert_called_once_with(Category, Category.id == test_id)
    mock_engine.delete.assert_called_once_with(existing_category)

@pytest.mark.asyncio
async def test_get_all_tutorials(tutorial_service_instance, mock_engine):
    mock_tutorials = [
        Tutorial(id=ObjectId(), title="Tut1", category_id=ObjectId(), content="C1", order=1),
        Tutorial(id=ObjectId(), title="Tut2", category_id=ObjectId(), content="C2", order=2)
    ]
    mock_engine.find.return_value = mock_tutorials

    tutorials = await tutorial_service_instance.get_all_tutorials()

    assert len(tutorials) == 2
    assert tutorials[0].title == "Tut1"
    mock_engine.find.assert_called_once_with(Tutorial)

@pytest.mark.asyncio
async def test_get_tutorials_by_category(tutorial_service_instance, mock_engine):
    test_category_id = ObjectId()
    mock_tutorials = [
        Tutorial(id=ObjectId(), title="Tut1", category_id=test_category_id, content="C1", order=1)
    ]
    mock_engine.find.return_value = mock_tutorials

    tutorials = await tutorial_service_instance.get_tutorials_by_category(test_category_id)

    assert len(tutorials) == 1
    assert tutorials[0].category_id == test_category_id
    mock_engine.find.assert_called_once_with(Tutorial, Tutorial.category_id == test_category_id)

@pytest.mark.asyncio
async def test_get_tutorial_by_id(tutorial_service_instance, mock_engine):
    test_id = ObjectId()
    mock_tutorial = Tutorial(id=test_id, title="TestTut", category_id=ObjectId(), content="TestContent", order=1)
    mock_engine.find_one.return_value = mock_tutorial

    tutorial = await tutorial_service_instance.get_tutorial_by_id(test_id)

    assert tutorial.title == "TestTut"
    mock_engine.find_one.assert_called_once_with(Tutorial, Tutorial.id == test_id)

@pytest.mark.asyncio
async def test_create_tutorial(tutorial_service_instance, mock_engine):
    mock_category_id = ObjectId()
    mock_engine.find_one.return_value = Category(id=mock_category_id, name="MockCat") # Mock category existence
    mock_engine.save.side_effect = lambda x: x

    tutorial = await tutorial_service_instance.create_tutorial(
        "NewTut", mock_category_id, "NewContent", 1
    )

    assert tutorial.title == "NewTut"
    assert tutorial.category_id == mock_category_id
    mock_engine.save.assert_called_once()

@pytest.mark.asyncio
async def test_update_tutorial(tutorial_service_instance, mock_engine):
    test_id = ObjectId()
    existing_tutorial = Tutorial(id=test_id, title="OldTut", category_id=ObjectId(), content="OldContent", order=1)
    mock_engine.find_one.side_effect = [
        existing_tutorial, # For finding the tutorial
        Category(id=ObjectId(), name="NewCat") # For checking new category existence
    ]
    mock_engine.save.side_effect = lambda x: x

    updated_tutorial = await tutorial_service_instance.update_tutorial(test_id, title="UpdatedTut")

    assert updated_tutorial.title == "UpdatedTut"
    mock_engine.find_one.assert_any_call(Tutorial, Tutorial.id == test_id)
    mock_engine.save.assert_called_once()

@pytest.mark.asyncio
async def test_delete_tutorial(tutorial_service_instance, mock_engine):
    test_id = ObjectId()
    existing_tutorial = Tutorial(id=test_id, title="TutToDelete", category_id=ObjectId(), content="C", order=1)
    mock_engine.find_one.return_value = existing_tutorial
    mock_engine.delete.return_value = None

    result = await tutorial_service_instance.delete_tutorial(test_id)

    assert result is True
    mock_engine.find_one.assert_called_once_with(Tutorial, Tutorial.id == test_id)
    mock_engine.delete.assert_called_once_with(existing_tutorial)