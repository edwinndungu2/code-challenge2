import os
import pytest
import sqlite3
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    os.environ["TESTING"] = "1"
    conn = get_connection()
    cursor = conn.cursor()
    
    # Reset schema
    cursor.executescript("""
        DROP TABLE IF EXISTS articles;
        DROP TABLE IF EXISTS authors;
        DROP TABLE IF EXISTS magazines;

        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        );

        CREATE TABLE articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        );
    """)
    
    conn.commit()
    conn.close()
    yield
    os.remove("test_articles.db")
