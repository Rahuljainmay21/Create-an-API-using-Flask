import mysql.connector as connection
conn = connection.connect(host="localhost",user="root", passwd="",use_pure=True)
cur = conn.cursor()
query = "SHOW DATABASES"
cur.execute(query)
print(cur.fetchall())
conn.close()

# mydb = connection.connect(host="localhost", database = 'student',user="root", passwd="",use_pure=True)
# query = "CREATE TABLE empdetails (name VARCHAR(30),empid VARCHAR(10))"
# cursor = mydb.cursor() #create a cursor to execute queries
# cursor.execute(query)
# mydb.close()