from pydantic import BaseModel
from typing import List

from levels.level_schema import LevelSchema

class TeamSchema(BaseModel):

    name: str
    levels: List[LevelSchema]


class TeamsSchema(BaseModel):
    """
        API validation schema
    """

    teams: List[TeamSchema]

