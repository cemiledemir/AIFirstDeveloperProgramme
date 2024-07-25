import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# API URL
API_URL = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=100"

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

def get_cat_facts():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def save_cat_facts(facts):
    for fact_data in facts:
        # Check if this fact already exists in the database
        existing_fact = session.query(CatFact).filter_by(fact=fact_data['text']).first()
        if not existing_fact:
            fact = CatFact(fact=fact_data['text'])
            session.add(fact)
    session.commit()


def view_cat_facts():
    facts = session.query(CatFact).all()
    print("\nCat Facts in the Database:")
    for fact in facts:
        print(f"{fact.id}: {fact.fact}")

def main():
    facts = get_cat_facts()
    if facts:
        save_cat_facts(facts)
        view_cat_facts()

if __name__ == "__main__":
    main()