# Cat Facts Project

This project fetches random cat facts from an API and stores them in a SQLite database. The stored cat facts can be viewed using a Streamlit application.

## Requirements

- Python 3.x
- `requests` library
- `sqlalchemy` library
- `streamlit` library

## Setup

1. Install the required packages:

    ```bash
    pip install -r requirements.txt

## Usage

1. Run the Streamlit application to view the stored cat facts:

    ```bash
    streamlit run cat_facts_app.py
   
## Project Structure
* cat_facts_app.py: The main script to fetch and save cat facts and Streamlit application to view the stored cat facts.
* requirements.txt: List of required packages.
* cat_facts.db: The SQLite database file