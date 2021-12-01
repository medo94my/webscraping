
Python - Sort Lists
===================


Sort List Alphanumerically
--------------------------


List objects have a `sort()` method that will sort the list alphanumerically, ascending, by default:



### Example


Sort the list alphabetically:



```python
thislist = ["orange", "mango", "kiwi", 
  "pineapple", "banana"]thislist.sort()
print(thislist)

```



### Example


Sort the list numerically:



```python
thislist = [100, 50, 65, 82, 23]thislist.sort()
print(thislist)

```


Sort Descending
---------------


To sort descending, use the keyword argument `reverse = True`:



### Example


Sort the list descending:



```python
thislist = ["orange", "mango", "kiwi", 
  "pineapple", "banana"]thislist.sort(reverse = True)
print(thislist)

```



### Example


Sort the list descending:



```python
thislist = [100, 50, 65, 82, 23]thislist.sort(reverse = True)
print(thislist)

```


