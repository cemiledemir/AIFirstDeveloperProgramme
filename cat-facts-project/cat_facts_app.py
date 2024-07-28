import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import streamlit as st
import pandas as pd

# API URL
API_URL = "https://cat-fact.herokuapp.com/facts"

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


# CSS for background color
def set_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFEBCC;
        }
        .card {
            background-color: white;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Streamlit app
def main():
    set_background_color()

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image('cat_facts.png')

    with col2:
        st.title('Cat Facts Viewer')

    # Get all facts from the database
    all_facts = session.query(CatFact).all()

    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame([(fact.id, fact.fact) for fact in all_facts], columns=['id', 'fact'])

    # Display total number of facts
    st.write(f"Total number of cat facts: {len(df)}")

    # Display data in a card-like format
    if not df.empty:
        for index, row in df.iterrows():
            st.markdown(
                f"""
                <div class="card">
                    <h3>Cat Fact {index + 1}</h3>
                    <p>{row['fact']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("No data available in the database.")


if __name__ == "__main__":
    main()
