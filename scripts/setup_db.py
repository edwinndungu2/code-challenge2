from lib.db.connection import get_connection

def setup_schema():
    conn = get_connection()
    with open("lib/db/schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

if __name__ == "__main__":
    setup_schema()
