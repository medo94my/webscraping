
Python - Variable Names
=======================


Variable Names
--------------



A variable can have a short name (like x and y) or a more descriptive name (age, carname, total\_volume).

Rules for Python variables:

* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)



### Example


Legal variable names:



```python
myvar = "John"my\_var = "John"\_my\_var = "John"myVar = "John"
  MYVAR = "John"myvar2 = "John"
```



### Example


Illegal variable names:



```python
2myvar = "John"my-var = "John"
  my var = "John"
```



Remember that variable names are case-sensitive



Multi Words Variable Names
--------------------------


Variable names with more than one word can be difficult to read.


There are several techniques you can use to make them more readable:


Camel Case
----------


Each word, except the first, starts with a capital letter:



```python
myVariableName = "John"

```

Pascal Case
-----------


Each word starts with a capital letter:



```python
MyVariableName = "John"

```

Snake Case
----------


Each word is separated by an underscore character:



```python
my\_variable\_name = "John"

```

