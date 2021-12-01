
Python Functions
================


A function is a block of code which only runs when it is called.


You can pass data, known as parameters, into a function.


A function can return data as a result.


Creating a Function
-------------------


In Python a function is defined using the def 
keyword:



### Example



```python
def my\_function():  print("Hello from a function")
```


Calling a Function
------------------


To call a function, use the function name followed by parenthesis:



### Example



```python
def my\_function():  print("Hello from a function")
my\_function()
```


Arguments
---------


Information can be passed into functions as arguments.


Arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma.



The following example has a function with one argument (fname).
When the function is called, we pass along a first name,
which is used inside the function to print the full name:




### Example



```python
def my\_function(fname):  print(fname + " Refsnes")
  my\_function("Emil")my\_function("Tobias")my\_function("Linus")
```



*Arguments* are often shortened to *args* in Python documentations.














If you try to call the function with 1 or 3 arguments, you will get an error:




















































