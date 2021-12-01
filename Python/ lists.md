
Python Lists
============



```python
mylist = ["apple", "banana", "cherry"]

```

List
----


Lists are used to store multiple items in a single variable.


Lists are one of 4 built-in data types in Python used to store collections of 
data, the other 3 are [Tuple](python_tuples.asp), 
[Set](python_sets.asp), and [Dictionary](python_dictionaries.asp), all with different qualities and usage.


Lists are created using square brackets:



### Example


Create a List:



```python
thislist = ["apple", "banana", "cherry"]
print(thislist)

```


List Items
----------


List items are ordered, changeable, and allow duplicate values.


List items are indexed, the first item has index `[0]`,
the second item has index `[1]` etc.


Ordered
-------


When we say that lists are ordered, it means that the items have a defined order, and that order will not change.


If you add new items to a list,
the new items will be placed at the end of the list.



**Note:** There are some [list methods](python_lists_methods.asp) that will change the order, but in general: the order of the items will not change.



Changeable
----------


The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


Allow Duplicates
----------------


Since lists are indexed, lists can have items with the same value:



### Example


Lists allow duplicate values:



```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

```


