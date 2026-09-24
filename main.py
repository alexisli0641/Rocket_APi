from fastapi import FastAPI, HTTPException, Depends
from services import Player, PlayerCreate
import services, models, schemas
from schemas import PlayerCreate
from db import engine, get_db
from sqlalchemy.orm import Session
from services import get_players 
from pydantic import BaseModel

app = FastAPI()


@app.get("/players/")
def read_players(db:Session = Depends(get_db)):
    return get_players(db=db)

@app.get("/players/{player_id}")
def get_player_by_id(player_id, db:Session = Depends(get_db)):
    player = db.query(Player).filter(Player.player_id == player_id).first()
    #if user requests an ID that doesnt exists
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    else:
        return player


@app.post("/players/", response_model = schemas.Player)
def create_new_player(data: PlayerCreate, db: Session = Depends(get_db)):
    player_instance = Player(**data.model_dump())
    db.add(player_instance)
    db.commit()
    db.refresh(player_instance)
    return player_instance

# Comment 