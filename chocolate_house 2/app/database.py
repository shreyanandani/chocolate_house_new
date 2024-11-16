# import sqlite3

# def get_db_connection():
#     conn = sqlite3.connect("chocolate_house.db")
#     conn.row_factory = sqlite3.Row
#     return conn

# def setup_database():
#     conn = get_db_connection()
#     with open("schema.sql", "r") as f:
#         conn.executescript(f.read())
#     conn.close()

import sqlite3
import os

# Function to establish a database connection
def get_db_connection():
    # Use _file_ instead of file to get the correct path to this script
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chocolate_house.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
    return conn

# Function to initialize the database schema
def setup_database():
    conn = get_db_connection()
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schema.sql")
    
    # Check if schema.sql exists
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found at: {schema_path}")

    # Execute schema SQL to set up tables
    with open(schema_path, "r") as f:
        conn.executescript(f.read())
    
    conn.commit()
    conn.close()