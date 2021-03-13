from fastapi_sqlalchemy import db

from levels.level_model import Level

from .team_model import Team

def get_team_and_level_data(team: str, level: str):
    """
        Get the name of the team, the name and minimum goals of the level by the team and level provided 
    """

    team_query = db.session.query(Team.name, Level.name, Level.goal).join(Level).filter(Team.name == team, Level.name == level).first()

    if not team_query:
        return None
    return team_query

def team_already_exists(team: str):
    """
        Validate that teams are not repeated if does, return true that the team already exists, otherwise return false
    """
    team_query =  db.session.query(Team).filter(Team.name == team).first()

    if team_query is None:
        return False
    return True

def level_exists_by_team_and_level(team: str, level: str):
    """
        Check if a level already exists by team.
        If does it returns True otherwise returns False 
    """

    team_query = db.session.query(Team.name, Level.name).join(Level).filter(Team.name == team, Level.name == level).first()
    
    if team_query is None:
        return False
    return True