from fastapi_sqlalchemy import db
from sqlalchemy import or_, and_

from levels.level_model import Level

from .team_model import Team

def get_min_goal_by_team(team: str, level: str):
    """

    """

    return db.session.query(Team.name, Level.name, Level.goal).join(Level).filter(Team.name == team, Level.name == level)
