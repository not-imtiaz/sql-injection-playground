# SQL Injection Playground

A small Flask and SQLite demo app that intentionally contains a SQL injection vulnerability so you can see how the flaw works in a controlled local environment.

## What this project does

This repo demonstrates a classic authentication-bypass vulnerability caused by building SQL queries with direct string interpolation.

- `app.py` starts a minimal login form backed by SQLite.
- `app_vulnerable.py` is a similar variant that prints the SQL being executed for easier learning and debugging.
- `exploit.py` sends a crafted request that takes advantage of the vulnerable query.

The goal is educational: understand the issue, observe the exploit, and then fix it by switching to parameterized queries.

## Features

- Minimal Flask web app
- SQLite database with a seeded `admin` user
- Intentional SQL injection vulnerability for learning
- Simple Python exploit script that attacks the local app
- Small codebase that is easy to inspect and modify

## Requirements

- Python 3.10+
- `pip`

Python dependencies:

- `Flask`
- `requests`

## Installation

Clone the repository and install the dependencies:

```bash
pip install flask requests
```

If you prefer using a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask requests
```

## Running the app

Start the vulnerable web app from the repository root:

```bash
python app.py
```

Then open the app in your browser at:

```text
http://127.0.0.1:5000/
```

You can also run the debug-heavy variant:

```bash
python app_vulnerable.py
```

## Running the exploit

In a second terminal, run:

```bash
python exploit.py
```

The exploit script sends a login request with a crafted username value that comments out the rest of the SQL condition.

## How the vulnerability works

The login code builds SQL like this:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

Because the values are inserted directly into the query string, an attacker can inject SQL syntax into the input fields and change the meaning of the statement.

A safe version would use placeholders instead:

```python
cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password),
)
```

## Example attack

One payload used by the exploit is:

```text
admin' --
```

This closes the quoted username value and comments out the remaining password check, which can cause the query to match the admin row without knowing the real password.

## Project structure

```text
app.py              # Main vulnerable Flask login app
app_vulnerable.py   # Variant with SQL debug output
exploit.py          # Python exploit script using requests
LICENSE             # MIT license
```

## Suggested improvements

If you want to turn this into a stronger learning resource, consider adding:

- A safe version of the app using parameterized queries
- Side-by-side vulnerable and fixed examples
- A reset script for the SQLite database
- Unit tests that demonstrate the exploit failing against the fixed version
- A short write-up showing the difference between string interpolation and prepared statements

## Security note

This project is intended for local educational use only. Do not expose it to the public internet.

## License

MIT License. See [LICENSE](LICENSE) for details.
