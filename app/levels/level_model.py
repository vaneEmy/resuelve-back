from sqlalchemy import Column, String, Integer, ForeignKey
from config import Base

class Level(Base):
    """
        Database model for Level table
    """

    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    goal = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)