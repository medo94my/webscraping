
Python - Unpack Tuples
======================


Unpacking a Tuple
-----------------


When we create a tuple, we normally assign values to it. This is called "packing" a tuple:



### Example


Packing a tuple:



```python
fruits = ("apple", "banana", "cherry")

```


But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":



### Example


Unpacking a tuple:



```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

```



**Note:** The number of variables must match the number of values in the tuple, 
 if not, you must use an asterisk to collect the remaining values as a list.


