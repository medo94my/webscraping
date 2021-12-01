
Python - Loop Tuples
====================


Loop Through a Tuple
--------------------


You can loop through the tuple items by using a `for` loop.



### Example


Iterate through the items and print the values:



```python
thistuple = ("apple", "banana", "cherry")
  for x in thistuple:  print(x)
```


Learn more about `for` loops in our [Python For Loops](python_for_loops.asp) Chapter.


Loop Through the Index Numbers
------------------------------


You can also loop through the tuple items by referring to their index number.


Use the `range()` and `len()` functions to create a suitable iterable.



### Example


Print all items by referring to their index number:



```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```


