import sqlite3

def migrate(conn):
    
    cursor = conn.cursor()
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL
                    )
                """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS transactions ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    nominal INTEGER NOT NULL,
                    type TEXT NOT NULL DEFAULT ('masuk')
                    )
                """)
    conn.commit()