# importing the base from db.py so that python can read and 
from backend.db import Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship 

# Define the table and base is the format as to how the schema is structured
class Player(Base):
    # table name from PG database
    __tablename__ = "players"

    # column name = Column(Variable type, index = runs specific queries, nullable = NOT NULL )
    player_id = Column(Integer, primary_key = True, index = True, nullable = False)
    player_name = Column(String, index = True, nullable = False)
    player_age = Column(Integer, index = True, nullable = False)
    height_inches = Column(Integer, index = True, nullable = False)
    # this is relationship command that helps associate
    stats = relationship("Player_Statistics", back_populates = "player")

class Player_Statistics(Base):
    __tablename__ = "player_statistics"

    stat_id = Column(Integer, primary_key = True, index = True, nullable = False)
    player_id = Column(Integer, ForeignKey("players.player_id"), index = True, nullable = False)
    season = Column(String, index = True, nullable = False)
    points_per_game = Column(Numeric(4,1), index = True, nullable = False)
    rebounds_per_game = Column(Numeric(4,1), index = True, nullable = False)
    assists_per_game = Column(Numeric(4,1), index = True, nullable = False)

    player = relationship("Player", back_populates = "stats")

        

