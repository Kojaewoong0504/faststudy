from odmantic import Model, Field, ObjectId
from typing import Optional
from datetime import datetime

class Tutorial(Model):
    title: str = Field(min_length=1, max_length=100)
    category_id: ObjectId
    content: str
    order: int = Field(ge=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "collection": "tutorials"
    }