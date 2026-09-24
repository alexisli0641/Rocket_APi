from fastapi import FastAPI, HTTPException, Depends
from backend.models import Player, Player_Statistics
from backend.services import Player, PlayerCreate
import backend.services as services, backend.models as models, backend.schemas as schemas
from backend.schemas import PlayerCreate, PlayerStatisticsCreate, Player_Statistics
from backend.db import engine, get_db
from sqlalchemy.orm import Session
from backend.services import get_players, get_player_statistics, create_player_statistic

app = FastAPI()


@app.get("/players/")
def read_players(db:Session = Depends(get_db)):
    return get_players(db=db)

@app.get("/player_statistics/")
def read_player_statistics(db:Session = Depends(get_db)):
    return get_player_statistics(db=db)


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
    return services.create_player(db = db  , data = data)

@app.post("/player_statistics,", response_model = schemas.PlayerStatisticsCreate)
def create_new_player_statistic(data: PlayerStatisticsCreate, db: Session =  Depends(get_db)):
    return services.create_player_statistic(db = db, data = data)

@app.delete("/players/{player_id}")
def delete_player(player_id:int, db: Session = Depends(get_db)):
    # query database to find player
    player_to_delete = db.query(models.Player).filter(models.Player.player_id == player_id).first()
    if not player_to_delete:
        raise HTTPException(status_code = 404, detail = "User does not exist")
    db.query(models.Player_Statistics).filter(models.Player_Statistics.player_id == player_id).delete()
    # tells database to delete record
    db.delete(player_to_delete)
    db.commit()

    return {"message":"Player successfully deleted.", "Delete User":player_to_delete}

@app.put("/player/{player_id}", response_model = schemas.Player)
def update_player(player_id:int, updated_data: schemas.PlayerCreate, db: Session = Depends(get_db)):
    player_update = db.query(models.Player).filter(models.Player.player_id == player_id).first()
    if not player_update:
        raise HTTPException(status_code = 404, detail = "User does not exist")

    update_data_dict = updated_data.model_dump()
    for field, value in update_data_dict.items():
        setattr(player_update, field, value)

    db.commit()
    db.refresh(player_update)

    return player_update