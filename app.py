from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize a dummy database


def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'secret123')")
    conn.commit()
    conn.close()


init_db()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # VULNERABLE: Direct string concatenation
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        return "Login Successful!" if user else "Login Failed!"

    return '''<form method="post">
                Username: <input name="username"><br>
                Password: <input name="password" type="password"><br>
                <input type="submit">
              </form>'''


if __name__ == '__main__':
    app.run(debug=True)
