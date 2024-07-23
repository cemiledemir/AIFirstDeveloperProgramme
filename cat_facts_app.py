import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# API URL
API_URL = "https://cat-fact.herokuapp.com/facts&quot"

# Database setup
engine = create_engine('sqlite:///cat_facts.db', echo=True)  # create connection to a SQLite database
Base = declarative_base()


# Define the CatFact model
class CatFact(Base):
    __tablename__ = 'cat_facts'

    id = Column(Integer, primary_key=True)
    fact = Column(String)


# Create the database and table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
