
How to Remove Duplicates From a Python List
===========================================


Learn how to remove duplicates from a List in Python.



### Example


Remove any duplicates from a List:



```python
mylist = ["a", "b", "a", "c", "c"]mylist = list(dict.fromkeys(mylist))
  print(mylist)
```


Example Explained
-----------------


First we have a List that contains duplicates:



### A List with Duplicates



**mylist = ["a", "b", "a", "c", "c"]**

mylist = list(dict.fromkeys(mylist))
print(mylist)



Create a dictionary, 
using the List items as keys. This will automatically remove any duplicates 
because dictionaries cannot have duplicate keys.



### Create a Dictionary




 mylist = ["a", "b", "a", "c", "c"]

mylist = list(**dict.fromkeys(mylist)**)
 print(mylist)


Then, convert the dictionary back into a list:



### Convert Into a List




 mylist = ["a", "b", "a", "c", "c"]

**mylist = list(**dict.fromkeys(mylist)**)**
print(mylist)


Now we have a List without any duplicates, and it has the same order as the 
original List.


Print the List to demonstrate the result



### Print the List




 mylist = ["a", "b", "a", "c", "c"]
 mylist = list(dict.fromkeys(mylist))
**print(mylist)**


