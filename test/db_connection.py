import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_mysql():
    try:
        connection = psycopg2.connect(
            host=os.getenv("RDS_ENDPOINT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER_RDS"),
            password=os.getenv("DB_PASSWORD")
        )

        if connection.closed == 0:
            print("Connected to PostgreSQL")
            return connection
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None
