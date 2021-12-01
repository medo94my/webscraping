
Python MySQL Create Table
=========================


Creating a Table
----------------


To create a table in MySQL, use the "CREATE TABLE" statement.


Make sure you define the name of the database when you create the connection



### Example


Create a table named "customers":



 import mysql.connectormydb = mysql.connector.connect(  host="localhost",
  
 user="*yourusername*",  password="*yourpassword*",
   database="mydatabase")mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), 
 address VARCHAR(255))")

If the above code was executed with no errors, you have now successfully 
created a table.


Check if Table Exists
---------------------


You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:



### Example


Return a list of your system's databases:



```python
import mysql.connectormydb = mysql.connector.connect(  host="localhost",  
  user="yourusername",  password="yourpassword",  database="mydatabase")mycursor = mydb.cursor()
  mycursor.execute("SHOW TABLES")for x in mycursor:  
  print(x)
```


