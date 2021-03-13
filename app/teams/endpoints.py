from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from levels.level_model import Level

from .team_model import Team
from .team_schema import TeamsSchema
from .services import team_already_exists

teamsRouter = APIRouter()

@teamsRouter.post('/teams')
def create_teams(teams: TeamsSchema):
    
    for team in teams.teams:
        
        if team_already_exists(team.name):
            raise HTTPException(status_code=400, detail="Team already exists")
        
        try:
            new_team = Team(name = team.name,)
            
            db.session.add(new_team)
            db.session.commit()
            db.session.refresh(new_team)
            
            for level in team.levels:
                new_level = Level(
                    name = level.level,
                    goal = level.goal,
                    team_id = new_team.id
                )

                db.session.add(new_level)
                db.session.commit()
        
            return { "message": "Teams added successfully" }

        except Exception as _:
            raise HTTPException(status_code=400, detail="Team not created")