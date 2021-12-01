
SQL SELECT DISTINCT Statement
=============================


The SQL SELECT DISTINCT Statement
---------------------------------


The `SELECT DISTINCT` statement is used to return only distinct 
(different) values.


Inside a table, a column often contains many duplicate values; and sometimes you 
only want to list the different (distinct) values.


### SELECT DISTINCT Syntax




```sql
SELECT DISTINCT column1, column2, ...
 FROM table\_name;

```

Demo Database
-------------


Below is a selection from the "Customers" table in the Northwind sample 
database:





| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany |
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico |
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico |
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK |
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden |



SELECT Example Without DISTINCT
-------------------------------


The following SQL statement selects all (including the duplicates) values from the "Country" column in the "Customers" table:



### Example



```sql
SELECT Country FROM Customers;


```


Now, let us use the `SELECT DISTINCT` statement and see the result.


