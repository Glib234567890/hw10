import sqlite3

connection = sqlite3.connect('hw10.sl3', timeout=5)
cursor = connection.cursor()

cursor.execute("create table users (City text, temperature text, time text)")

current_time = '15.11.2025'

cursor.execute("insert into users (City, temperature, time) values ('Київ', '-4°C', ?)", (current_time,))

cursor.execute("select * from users")
print(cursor.fetchall())

connection.commit()
