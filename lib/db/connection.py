import sqlite3

def get_connection():
    conn = sqlite3.connect("articles.db")
    conn.row_factory = sqlite3.Row
    return conn


import os
import sqlite3

def get_connection():
    db_name = "test_articles.db" if os.getenv("TESTING") else "articles.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn
