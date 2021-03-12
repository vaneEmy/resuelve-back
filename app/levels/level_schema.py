from pydantic import BaseModel, Field
from typing import Optional

class LevelSchema(BaseModel):
    """
        API validation schema
    """

    level: str 
    goal: int    