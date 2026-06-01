import sqlite3

def get_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # WHY: Use parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Review for similar patterns in the file

def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # WHY: Use parameterized query to prevent SQL injection
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Add more functions as needed, ensuring all SQL queries are parameterized.