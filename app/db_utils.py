import sqlite3
import datetime

def create_db():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS price(id INTEGER PRIMARY KEY AUTOINCREMENT, price REAL, timestamp TEXT)")
    con.close()

def db_purge(older_than=365):
    now = datetime.datetime.now(datetime.UTC)
    limit = now - datetime.timedelta(days=int(older_than))
    condition = limit.strftime('%Y-%m-%d %H:%M')

    con = sqlite3.connect("demo_database.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM price WHERE timestamp LIKE {condition}%")
    con.commit()
    con.close()

def db_create(price):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    timestamp = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO price VALUES (?,?,?)", (None, float(price), str(timestamp)))
    con.commit()
    con.close()

def db_read(limit):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT * FROM price ORDER BY id DESC LIMIT {int(limit)}")
    raw_data = res.fetchall()
    con.close()
    data_list = []
    for x in raw_data:
        data_list.append(x[1])
    return data_list
