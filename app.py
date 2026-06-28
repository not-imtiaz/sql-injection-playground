from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)


def init_db()


conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin','secret123')")
conn.commit()
conn.close()


init_db()


@app.route('/'), methods = ['GET', 'POST'])
    def login():
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']

        conn= sqlite3.connect('users.db')
        crursor= conn.cursor()

        query= f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user= cursor.fetchone()
        conn.close()

        return "Login Successful" if user else "Login Failed"

    return '''<form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>'''

    if __name__ == '__main__':
    app.run(debug=True)
