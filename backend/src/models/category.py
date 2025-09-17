from odmantic import Model, Field
from typing import Optional

class Category(Model):
    name: str = Field(min_length=1, max_length=50)
    description: Optional[str] = Field(default=None, max_length=200)

    model_config = {
        "collection": "categories"
    }
