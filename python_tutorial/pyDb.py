import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="brothers",
  database="mydatabase"
#   database name is  used when perticular database needed while accessing all mysql db should not mention database name
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE if not exists mydatabase")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)


# for tables above database name in connector is mandate
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

mycursor.execute("create table if not exists customers (name varchar(20),adrs varchar(30))")
sql = "INSERT INTO customers (name, adrs) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
print("1 record inserted, ID:", mycursor.lastrowid)



