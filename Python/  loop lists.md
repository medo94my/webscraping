
Python - Loop Lists
===================


Loop Through a List
-------------------


You can loop through the list items by using a `for` 
loop:



### Example


Print all items in the list, one by one:



```python
thislist = ["apple", "banana", "cherry"]
  for x in thislist:  print(x)
```


Learn more about `for` loops in our [Python For Loops](python_for_loops.asp) Chapter.


Loop Through the Index Numbers
------------------------------


You can also loop through the list items by referring to their index number.


Use the `range()` and
`len()` functions to create a suitable iterable.



### Example


Print all items by referring to their index number:



```python
thislist = ["apple", "banana", "cherry"]for i 
  in range(len(thislist)):
 
print(thislist[i])
```


The iterable created in the example above is `[0, 1, 2]`.


