from typing import Optional
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI

from config import DB_URL, Base
from teams.endpoints import teamsRouter
from players.endpoints import playersRouter

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DB_URL, engine_args={"connect_args": {"check_same_thread": False }})

with db():
    Base.metadata.create_all(bind=db.session.get_bind())

@app.get('/')
def check_status():
    return { "status": "Ok" }

app.include_router(teamsRouter)
app.include_router(playersRouter)