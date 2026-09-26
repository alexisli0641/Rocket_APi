# CRUD Operations are setup here

from backend.models import Player, Player_Statistics
from sqlalchemy.orm import Session
from backend.schemas import PlayerCreate, PlayerStatisticsCreate


# Define function to create a player entry in database

def create_player(db:Session, data: PlayerCreate):
    player_instance = Player(**data.model_dump())
    db.add(player_instance)
    db.commit()
    db.refresh(player_instance)
    return player_instance

def create_player_statistic(db: Session, data:PlayerStatisticsCreate):
    player_statistic_instance = Player_Statistics(**data.model_dump())
    db.add(player_statistic_instance)
    db.commit()
    db.refresh(player_statistic_instance)
    return player_statistic_instance

# This function gets all player statistics
def get_players(db: Session):
    return db.query(Player).all()

def get_player_statistics(db:Session):
    return db.query(Player_Statistics).all()

