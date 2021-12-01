
Python Syntax
=============




Execute Python Syntax
---------------------


As we learned in the previous page, Python syntax can be executed by writing directly in the Command Line:




 >>> print("Hello, World!")
 Hello, World!
 




On this page
------------


[Execute Python Syntax](#execute_python_syntax)
[Python Indentation](#python_indentation)
[Python Variables](#python_variables)
[Python Comments](#python_comments)
[Exercises](#exercises)



Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:




 C:\Users\*Your Name*>python myfile.py
 

Python Indentation
------------------


Indentation refers to the spaces at the beginning of a code line.


Where in other programming languages the indentation in code is for readability 
only, the indentation in Python is very important.


Python uses indentation to indicate a block of code.



### Example



```python
if 5 > 2: 
print("Five is greater than two!")

```


Python will give you an error if you skip the indentation:



### Example


Syntax Error:



```python
if 5 > 2:
print("Five is greater than two!")

```


The number of spaces is up to you as a programmer, but it has 
to be at least one.



### Example



```python
if 5 > 2: print("Five is greater than two!") 
if 5 > 2:        print("Five is greater than two!") 

```


You have to use the same number of spaces in the same block of code, 
otherwise Python will give you an error:



### Example


Syntax Error:



```python
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than 
  two!")
```


