# schemas to validate complex data structures with pydantic

from pydantic import BaseModel

# Define first schema to inherit BaseModel
# goes through and validates data
class PlayerBase(BaseModel):
    player_name: str
    player_age: int
    height_inches: int

# Schema for creating a player profile instance
class PlayerCreate(PlayerBase):
    player_name: str
    player_age: int
    height_inches: int


# Define get book
# Here we need the ID of player to update or get player 
class Player(PlayerBase):
    player_id : int

    class Config:
        from_attributes = True 

class PlayerStatsBase(BaseModel):
    season: str
    points_per_game: float
    assists_per_game: float
    rebounds_per_game: float

# Schema for creating player statistics instance 
class PlayerStatisticsCreate(PlayerStatsBase):
    player_id: int

# Define get book
# Here we need the ID of player to update or get player 
class Player_Statistics(PlayerStatsBase):
    stat_id : int
    player_id: int

    class Config:
        from_attributes = True
    
