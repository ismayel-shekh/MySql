#create database
import mysql.connector
mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "ismayel1234"
)
print(mydbconnection)
db_name = "python_test_bd"
mycursor = mydbconnection.cursor()
sqlquery = "create database " + db_name
mycursor.execute(sqlquery)
# crate a table