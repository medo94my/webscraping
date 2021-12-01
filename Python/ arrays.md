
Python Arrays
=============



**Note:** Python does not have built-in support for Arrays, 
 but [Python Lists](python_lists.asp) can be used instead.



Arrays
------



**Note:** This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import
 a library, like the [NumPy library](numpy/default.asp).



Arrays are used to store multiple values in one single variable:



### Example


Create an array containing car names:



```python
cars = ["Ford", "Volvo", "BMW"]
```


What is an Array?
-----------------


An array is a special variable, which can hold more than one value at a time.


If you have a list of items (a list of car names, for example), storing the 
cars in single variables could look like this:




 car1 = "Ford"
 car2 = "Volvo"
 car3 = "BMW"

However, what if you want to loop through the cars and find a specific one? 
And what if you had not 3 cars, but 300?


The solution is an array!


An array can hold many values under a single name, and you can 
access the values by referring to an index number.


Access the Elements of an Array
-------------------------------


You refer to an array element by referring to the *index number*.



### Example


Get the value of the first array item:



```python
x = cars[0]
```



### Example


Modify the value of the first array item:



```python
cars[0] = "Toyota"
```


The Length of an Array
----------------------


Use the `len()` method to return the length of 
an array (the number of elements in an array).



### Example


Return the number of elements in the `cars` 
array:



```python
x = len(cars)
```



**Note:** The length of an array is always one more than the highest array index.


