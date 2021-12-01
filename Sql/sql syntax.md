
SQL Syntax
==========


Database Tables
---------------


A database most often contains one or more tables. Each table is identified 
by a name (e.g. "Customers" or "Orders"). Tables contain records (rows) with 
data.


In this tutorial we will use the well-known Northwind sample database 
(included in MS Access and MS SQL Server).


Below is a selection from the "Customers" table:





| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico |
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico |
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK |
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |




The table above contains five records (one for each customer) and seven columns 
(CustomerID, CustomerName, ContactName, Address, City, PostalCode, and Country).


SQL Statements
--------------


Most of the actions you need to perform on a database are done with SQL 
statements.


The following SQL statement selects all the records in the "Customers" table:



### Example



```sql
SELECT * FROM Customers;


```


In this tutorial we will teach you all about the different SQL statements.


