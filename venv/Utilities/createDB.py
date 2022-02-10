import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

dropSQL = "DROP database IF EXISTS MYDATABASE_NEW"
#Doping database MYDATABASE if already exists.
cursor.execute(dropSQL)

#Preparing query to create a database
createSQL = "CREATE database MYDATABASE_NEW";

#Creating a database
cursor.execute(createSQL)

#Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

#Closing the connection
conn.close()