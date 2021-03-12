from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from .player_schema import PlayersSchema
from .services import create_player

from teams.services import get_min_goal_by_team

playersRouter = APIRouter()

@playersRouter.post('/salaries/calculation')
def calculate_salaries(players: PlayersSchema):
    
    teams = dict()
    

    for player in players.jugadores:
        if teams.get(player.equipo):
            players = teams.get(player.equipo)
            players.append(create_player(player.nombre, player.nivel, player.goles, player.sueldo, player.bono, player.equipo))
            teams[player.equipo] = players
             
        else:
            players_list = []
            players_list.append(create_player(player.nombre, player.nivel, player.goles, player.sueldo, player.bono, player.equipo))
            teams[player.equipo] = players_list

    for players in teams.values():
        for player in players:
            print(player.get('nombre'))
        
    return { "message": "Ok"}