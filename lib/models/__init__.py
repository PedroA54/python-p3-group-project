import sqlite3

CONN = sqlite3.connect("lib/data/data.csv")
CURSOR = CONN.cursor()
