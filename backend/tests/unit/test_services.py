from src.services.tutorial_service import TutorialService
from src.models.tutorial import Category, Tutorial

class TestTutorialService:
    def setup_method(self):
        # Re-initialize the service for each test to ensure isolation
        self.service = TutorialService()

    def test_get_all_categories(self):
        categories = self.service.get_all_categories()
        assert isinstance(categories, list)
        assert len(categories) > 0  # Assuming some categories exist in _DB
        assert all(isinstance(c, Category) for c in categories)
        # You can add more specific assertions based on your _DB content
        assert categories[0].id == "project-structure"

    def test_get_tutorial_by_id_exists(self):
        tutorial_id = "class-based-services"
        tutorial = self.service.get_tutorial_by_id(tutorial_id)
        assert isinstance(tutorial, Tutorial)
        assert tutorial.id == tutorial_id
        assert tutorial.title == "Implementing Class-Based Services"

    def test_get_tutorial_by_id_not_exists(self):
        tutorial_id = "non-existent-tutorial"
        tutorial = self.service.get_tutorial_by_id(tutorial_id)
        assert tutorial is None
