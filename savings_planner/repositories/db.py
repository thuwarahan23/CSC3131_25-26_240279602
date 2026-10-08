# db.py

import sqlite3
from pathlib import Path

DB_Path = "savings.db"

def get_conn():
    conn = sqlite3.connect(DB_Path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    schema = (Path(__file__).parent / "schema.sql").read_text()
    with get_conn() as conn:
        conn.executescript(schema)