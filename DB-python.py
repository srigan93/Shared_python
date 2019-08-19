import mysql.connector;
connection = mysql.connector.connect(host='localhost',database='my_table',user='root',password='root')
cur = connection.cursor();
cur.execute("Select * from supply;")
data = cur.fetchall();
for row in data:
    print(row)
connection.commit()
connection.close()
