
SQL SELECT Statement
====================


The SQL SELECT Statement
------------------------


The `SELECT` statement is used to select data from a database.


The data returned is stored in a result table, called the result-set.


### SELECT Syntax




```sql
SELECT column1, column2, ...
FROM table\_name;

```

Here, column1, column2, ... are the field names of the table you want to 
select data from. If you 
want to select all the fields available in the table, use the following syntax:




```sql
SELECT * FROM table\_name;

```

Demo Database
-------------


Below is a selection from the "Customers" table in the Northwind sample database:





| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico |
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico |
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK |
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |



SELECT Column Example
---------------------


The following SQL statement selects the "CustomerName" and "City" columns 
from the "Customers" table:



### Example



```sql
SELECT CustomerName, City FROM Customers;


```


SELECT * Example
----------------


The following SQL statement selects all the columns from the "Customers" 
table:



### Example



```sql
SELECT * FROM Customers;


```



