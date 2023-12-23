import mysql.connector
mydb  = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    passwd = "ismayel1234"
)
print(mydb)
