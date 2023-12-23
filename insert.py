#create database
import mysql.connector
db_name = "python_test_db"
mydbconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "ismayel1234",
    database = db_name
)
mycursor = mydbconnection.cursor()
sqlquery = """
    insert into Student(roll,name)
    values('101', 'ismayel')
    
"""
mycursor.execute(sqlquery)
mydbconnection.commit()
print('INSERT TABLE SUCCESSFUL')