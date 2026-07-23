import sqlite3
from pathlib import Path

database_path = Path(__file__).with_name("data.db")

connection = sqlite3.connect(database_path, check_same_thread=False)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL, 
            author TEXT NOT NULL,
            publisher TEXT NOT NULL, 
            location TEXT NOT NULL,
            year INTEGER NOT NULL,
            pages INTEGER NOT NULL

        );
""")

connection.commit()

