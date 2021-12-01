
Python - Access Dictionary Items
================================


Accessing Items
---------------


You can access the items of a dictionary by referring to its key name, inside 
square brackets:



### Example


Get the value of the "model" key:



```python
thisdict =	{

  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

```


There is also a method called `get()` that will give you the same result:



### Example


Get the value of the "model" key:



```python
x = thisdict.get("model")

```


Get Keys
--------


The `keys()` method will return a list of all the keys in the dictionary.



### Example


Get a list of the keys:



```python
x = thisdict.keys()
```


The list of the keys is a *view* of the dictionary, meaning that any 
changes done to the dictionary will be reflected in the keys list.



### Example


Add a new item to the original dictionary, and see that the keys list gets 
updated as well:



```python
car = {
"brand": "Ford","model": "Mustang","year": 1964}

x = car.keys()print(x) #before the changecar["color"] = 
  "white"print(x) #after the change
```


