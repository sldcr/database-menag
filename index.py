import mysql.connector as mc
from datetime import datetime

# connect to database
conn = mc.connect(host='localhost', user='root', password='123456789!', db='menagerie')

# cursor to perform operations
c = conn.cursor()

# execute SQL query
c.execute('SELECT name, birth FROM pet')

# print results
print("name | birth | MONTH(birth)")
for record in c.fetchall():
    name, birth = record
    month = birth.month  # Access the month attribute directly
    print(f"{name} | {birth} | {month}")
