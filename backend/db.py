from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

# connecting to database
# database_url = "postgresql://username:password@host:port/database"

database_url = "postgresql://postgres:123456@localhost:5432/postgres"

# create the engine 
engine = create_engine(database_url)

# When you create a session, this rep picks up the phone, talks to the database, 
# handles your requests (adds, updates, deletes data), and hangs up when done.
# Helps perform actions onto database
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# help create tables in python 
Base = declarative_base()
metadata = Base.metadata 
# define function to perform actions... opens and closes db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# function to help create our tables
# equivalent to running CREATE TABLE in SQL
# def create_table():
    # Base.metadata.create_all(bind = engine)