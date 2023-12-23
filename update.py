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
update Student
set name = 'modon'
where name = 'ismayel'
    
"""
mycursor.execute(sqlquery)
mydbconnection.commit()
print('UPDATE TABLE SUCCESSFUL')