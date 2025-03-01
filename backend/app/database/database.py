import pymysql

connection = pymysql.connect(host = "localhost", user = "root", passwd = "", database = "transplants")
cursor = connection.cursor()
query = "select * from employee"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()