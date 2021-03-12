from pydantic import BaseModel
from typing import List, Optional

class PlayerSchema(BaseModel):
    """
        API validation schema for player
    """
    nombre: str
    nivel: str
    goles: int
    sueldo: int
    bono: int
    sueldo_completo: Optional[str]
    equipo: str

class PlayersSchema(BaseModel):
    """
        API validation schema for Players
    """

    jugadores: List[PlayerSchema]