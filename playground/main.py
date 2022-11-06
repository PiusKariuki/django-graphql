import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

print(db)
my_cursor = db.cursor()

# my_cursor.execute("CREATE DATABASE  testdatabase")