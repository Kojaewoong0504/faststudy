from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    """Represents a grouping of related learning tutorials."""
    id: str
    name: str
    description: str

class Tutorial(BaseModel):
    """Represents a single learning module or topic."""
    id: str
    category_id: str
    title: str
    content: str
    author: Optional[str] = None
