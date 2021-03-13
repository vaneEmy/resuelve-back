
from teams.services import get_team_and_level_data

def create_player(name, level, goals, salary, bono, team):
    """
        We get the minimum of goals by team and level that the player has
        then, we create a Player object with the following information: Name, goals, minimum goals, salary, bono and team   
    """

    team_query = get_team_and_level_data(team, level)

    if team_query is None:
        return None
    
    return {   
        "nombre": name,
        "goles_minimos": team_query[2], # The 2nd element is the number of goals of the team that the player belongs to
        "goles": goals,
        "sueldo": salary,
        "bono":  bono,
        "equipo": team 
    }