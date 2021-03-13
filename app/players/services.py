
from teams.services import get_min_goal_by_team

def create_player(name, level, goals, salary, bono, team):
    """
        We get the minimum of goals by team and level that the player has
        then, we create a Player object with the following information: Nivel, goles, sueldo, bono, goles mínimos  
    """

    team_query = get_min_goal_by_team(team, level)
            
    return {   
        "nombre": name,
        "goles_minimos": team_query[0][2],
        "goles": goals,
        "sueldo": salary,
        "bono":  bono,
        "equipo": team 
    }