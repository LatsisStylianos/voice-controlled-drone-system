import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create a table for users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Insert a new user into the database
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # If the username already exists, return False
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Check if the username and password match
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()
    return user is not None