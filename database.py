import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("telecom.db")
cursor = conn.cursor()

# Create 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mobile_no TEXT UNIQUE NOT NULL,
    plan TEXT NOT NULL
)
""")

# Create 'usage' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS usage (
    user_id INTEGER,
    balance REAL,
    data_left_gb REAL,
    last_recharge_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

# Insert Dummy Data
cursor.executemany("INSERT INTO users (name, mobile_no, plan) VALUES (?, ?, ?)", [
    ("John Doe", "987XXXX210", "Unlimited 599"),
    ("Alice Smith", "876XXXX109", "Basic 299"),
    ("Disney Watt", "911XXXX593", "Medium 399"),
    ("Sam smith", "958XXXX239", "Basic 299"),
    ("Sabrina Carpenter", "909XXXX969", "Yearly 2999"),    
])

cursor.executemany("INSERT INTO usage (user_id, balance, data_left_gb, last_recharge_date) VALUES (?, ?, ?, ?)", [
    (1, 50.0, 1.5, "2025-03-20"),
    (2, 120.0, 2.0, "2025-03-18"),
    (3, 110.0, 2.0, "2025-04-15"),
    (4, 90.0, 2.0, "2025-03-03"),
    (5, 1020.0, 2.0, "2026-01-18"),
])

# Commit and close connection
conn.commit()
conn.close()
print("Database setup complete with dummy data.")
