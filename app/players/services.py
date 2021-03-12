
from teams.services import get_min_goal_by_team

def create_player(name, level, goals, salary, bono, team):
    """
    """

    team_query = get_min_goal_by_team(team, level)
            
    return {   "nombre": name,
        "nivel": level,
        "goles": goals,
        "sueldo": salary,
        "bono":  bono,
        "minimo_goles": team_query[0][2] 
    }