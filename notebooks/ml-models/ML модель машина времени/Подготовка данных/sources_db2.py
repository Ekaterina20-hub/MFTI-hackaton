import pandas as pd
from sqlalchemy import create_engine, text

def connectDB(db_string):
    try:
        engine = create_engine(db_string)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Postgresql connected.")
        return engine

# def runQuery(query, engine):
#     return pd.read_sql_query(query, engine)
