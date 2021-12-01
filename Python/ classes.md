
Python Classes and Objects
==========================


Python Classes/Objects
----------------------


Python is an object oriented programming language.


Almost everything in Python is an object, with its properties and methods.


A Class is like an object constructor, or a "blueprint" for creating objects.


Create a Class
--------------


To create a class, use the keyword `class`:



### Example


Create a class named MyClass, with a property named x:



```python
class MyClass:  x = 5
```


Create Object
-------------


Now we can use the class named MyClass to create objects:



### Example


Create an object named p1, and print the value of x:



```python
p1 = MyClass()print(p1.x)
```


The \_\_init\_\_() Function
---------------------------


The examples above are classes and objects in their simplest form, and are 
not really useful in real life applications.


To understand the meaning of classes we have to understand the built-in \_\_init\_\_() 
function.


All classes have a function called \_\_init\_\_(), which is always executed when 
the class is being initiated.


Use the \_\_init\_\_() function to assign values to object properties, or other 
operations that are necessary to do when the object 
is being created:



### Example


Create a class named Person, use the \_\_init\_\_() function to assign values 
for name and age:



```python
class Person:  def \_\_init\_\_(self, name, age):    
  self.name = name    self.age = agep1 = Person("John", 
  36)
print(p1.name)print(p1.age)
```



**Note:** The `__init__()` function is called automatically every time the class is being used to create a new object.



