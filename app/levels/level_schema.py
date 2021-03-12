from pydantic import BaseModel

class LevelSchema(BaseModel):
    """
        API validation schema
    """

    level: str 
    goal: int    