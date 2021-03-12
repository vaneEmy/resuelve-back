from sqlalchemy import Column, String, Integer
from config import Base


class Team(Base):
    """
        Database model for Team table
    """

    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

