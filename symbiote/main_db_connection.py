from turtle import st
from mysqlx import Row
import psycopg2
import datetime

DB_NAME = "dztyhjzl"
DB_USER = "dztyhjzl"
DB_PASS = "1fZLeEypTQjGX7SohwUr5gYT9YYu1PcB"
DB_HOST = "hansken.db.elephantsql.com"
DB_PORT = "5432"
conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                        host=DB_HOST, port=DB_PORT)
def confirmation():
    print("Database connected successfully")

def add(emp_id):
    date=datetime.date.today()
    time=datetime.datetime.now().time()

    uid=1
    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM symbiote_attendence_area")
    rows = cur.fetchall()
    uid=str(rows[0][0]+1 if rows[0][0] else uid)
    query = "INSERT INTO symbiote_attendence_area (id,employee_id,date,time) VALUES ("+uid+","+str(emp_id)+"," + "'" + str(date) + "'" + "," + "'" + str(time) + "'" + ");"
    print(query)
    cur.execute(query)
    conn.commit()

def delete_attendence():
    curr=conn.cursor()
    curr.execute("DELETE FROM symbiote_attendence_area")
    conn.commit()
