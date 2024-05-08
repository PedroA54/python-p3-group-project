import sqlite3

CONN = sqlite3.connect("lib/nba.db")
CURSOR = CONN.cursor()
