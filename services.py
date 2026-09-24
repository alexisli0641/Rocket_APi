# CRUD Operations are setup here

from models import Player, Player_Statistics
from sqlalchemy.orm import Session
from schemas import PlayerCreate, PlayerStatisticsCreate


# Define function to create a player entry in database

def create_player(db:Session, data: PlayerCreate):
    player_instance = Player(**data.model_dump())
    db.add(player_instance)
    db.commit()
    db.refresh(player_instance)
    return player_instance

def get_players(db: Session):
    return db.query(Player).all()

