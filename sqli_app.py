from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'password123'))
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Vulnerable SQL Query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    user = c.fetchone()

    if user:
        return jsonify({"message": "Logged in!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/secure_login', methods=['POST'])
def secure_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Simple input validation (whitelisting approach)
    if not username.isalnum() or not password.isalnum():
        return jsonify({"message": "Invalid input"}), 400

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    user = c.fetchone()

    if user:
        return jsonify({"message": "Logged in!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
