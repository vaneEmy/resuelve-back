from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from .player_schema import PlayersSchema

from teams.services import get_min_goal_by_team

playersRouter = APIRouter()

@playersRouter.post('/salaries/calculation')
def calculate_salaries(players: PlayersSchema):
    
    teams = dict()
    players_list = []
    print(len(players.jugadores))
    for player in players.jugadores:
        print(player.equipo)    

        if teams.get(player.equipo):
            print("El equipo ya existe en el diccionario")
            
        else:
            print("El equipo no existe en el diccionario")
            print(player.nivel)
            
            team_query = get_min_goal_by_team(player.equipo, player.nivel)
            
            print(team_query[0][2])

            players_list.append({ 
                "nombre": player.nombre,
                "nivel": player.nivel,
                "goles": player.goles,
                "sueldo": player.sueldo,
                "bono":  player.bono,
                "minimo_goles": team_query[0][2] 
            })
            
            teams[player.equipo] = players_list

        return { "message": "Ok"}