from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from .player_schema import PlayersSchema
from .services import create_player

playersRouter = APIRouter()

@playersRouter.post('/salaries/calculation')
def calculate_salaries(players: PlayersSchema):
    
    teams = dict()
    new_players_list = []
    
    # We create a dictionary of teams which every team has players with their information and the  minimum goals by their level
    for player in players.jugadores:
        # We verify if the team exists in the key of the dictionary 
        if teams.get(player.equipo):
            players_list = teams.get(player.equipo)
            players_list.append(create_player(player.nombre, player.nivel, player.goles, player.sueldo, player.bono, player.equipo))
            teams[player.equipo] = players_list
        else:
            players_list = []
            players_list.append(create_player(player.nombre, player.nivel, player.goles, player.sueldo, player.bono, player.equipo))
            teams[player.equipo] = players_list

    
    # We iterate over the teams dictionary in order to calculate the total of goals by players in the team, the bono and the total salary 
    for players_values in teams.values():
        
        # We sum all goals and minimum goals by team  
        team_goals = sum(p.get('goles') for p in players_values)
        total_goals = sum(p.get('goles_minimos') for p in players_values)
        
        team_porcentage = (team_goals*100)/total_goals

        # Add players list to a new list
        new_players_list.extend(players_values)
        
        for player_value in players_values:
            individual_porcentage = (player_value.get('goles')*100) / player_value.get('goles_minimos')
            
            # Calculate team and individual 
            team_goal = ((player_value.get('bono') / 2) * team_porcentage) / 100
            individual_goal = ((player_value.get('bono') / 2) * individual_porcentage) / 100
            
            # Calculate the total salary and round decimals
            total_salary = round(player_value.get('sueldo') + (team_goal +  individual_goal), 2)
            
            # Add total salary to player object
            player_value["sueldo_completo"] = total_salary

    return { "jugadores": new_players_list}