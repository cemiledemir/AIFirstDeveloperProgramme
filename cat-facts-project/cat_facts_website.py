import streamlit as st
import sqlite3
import pandas as pd


# Function to get data from the database
def get_cat_facts():
    conn = sqlite3.connect('cat_facts.db')
    query = "SELECT * FROM cat_facts"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# Streamlit app
def main():
    st.title('Cat Facts Database Viewer')

    # Fetch data
    df = get_cat_facts()

    # Display total number of facts
    st.write(f"Total number of cat facts: {len(df)}")

    # Display the dataframe
    st.dataframe(df)

    # Allow user to select a specific fact
    fact_id = st.selectbox('Select a fact ID to view:', df['id'].tolist())

    if fact_id:
        selected_fact = df[df['id'] == fact_id]['fact'].values[0]
        st.write(f"Fact #{fact_id}: {selected_fact}")


if __name__ == "__main__":
    main()
