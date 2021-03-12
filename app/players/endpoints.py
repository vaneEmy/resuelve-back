from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from .player_schema import PlayersSchema
from .services import create_player

playersRouter = APIRouter()

@playersRouter.post('/salaries/calculation')
def calculate_salaries(players: PlayersSchema):
    
    teams = dict()
    
    # We create a dictionary of teams which every team has players with their information and the  minimum of goals by their level
    for player in players.jugadores:
        if teams.get(player.equipo):
            players_list = teams.get(player.equipo)
            players_list.append(create_player(player.nombre, player.nivel, player.goles, player.sueldo, player.bono, player.equipo))
            teams[player.equipo] = players_list
             
        else:
            players_list = []
            players_list.append(create_player(player.nombre, player.nivel, player.goles, player.sueldo, player.bono, player.equipo))
            teams[player.equipo] = players_list

    
    # We iterate over the teams dictionary in order to calculate team and individual percentage 
    for players in teams.values():
        
        team_goals = sum(p.get('goles') for p in players)
        total_goals = sum(p.get('minimo_goles') for p in players)
        
        team_porcentage = (team_goals*100)/total_goals

        for player in players:
            individual_porcentage = (player.get('goles')*100) / player.get('minimo_goles')
            
            team_goal = ((player.get('bono') / 2) * team_porcentage) / 100
            individual_goal = ((player.get('bono') / 2) * individual_porcentage) / 100
            
            total_bono = team_goal +  individual_goal

            total_salary = player.get('sueldo') + total_bono
            print(total_salary)
            
            
    return { "message": "Ok"}