
Python Modules
==============


What is a Module?
-----------------


Consider a module to be the same as a code library.


A file containing a set of functions you want to include in your application.


Create a Module
---------------


To create a module just save the code you want in a file with the file extension `.py`:



### Example


Save this code in a file named `mymodule.py`



```python
def greeting(name):  print("Hello, " + name)
```


Use a Module
------------


Now we can use the module we just created, by using the `import` statement:



### Example


Import the module named mymodule, and call the greeting function:



```python
import mymodulemymodule.greeting("Jonathan")

```



**Note:** When using a function from a module, use the syntax: *module\_name.function\_name*.



Variables in Module
-------------------


The module can contain functions, as already described, but also variables of 
all types (arrays, dictionaries, objects etc):



### Example


Save this code in the file `mymodule.py`



```python
person1 = {
  "name": "John",  "age": 36,  
  "country": "Norway"}

```



### Example


Import the module named mymodule, and access the person1 dictionary:



```python
import mymodulea = mymodule.person1["age"]print(a)
```


