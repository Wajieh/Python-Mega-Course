import sqlite3

#Create connection
connection = sqlite3.connect("data1.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT band FROM events WHERE date = '2088.10.17'")
print(cursor.fetchall())

# #Insert new rows
# new_rows = [('Cats', 'Cat City', '2088.10.17'),('Cow', 'Cow City', '2088.10.17')]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
# connection.commit()