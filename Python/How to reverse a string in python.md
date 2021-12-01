
How to Reverse a String in Python
=================================


Learn how to reverse a String in Python.


There is no built-in function to reverse a String in Python.


The fastest (and easiest?) way is to use a slice that steps backwards, `-1`.



### Example


Reverse the string "Hello World":



```python
txt = "Hello World"[::-1]print(txt)
```


Example Explained
-----------------


We have a string, "Hello World", which we want to reverse:



### The String to Reverse



txt = **"Hello World"**[::-1]
 print(txt)

Create a slice that starts at the end of the string, and moves backwards.


In this particular example, the slice statement `[::-1]` means start at 
the end of the string and end at position 0, move with the 
step `-1`, *negative* one, which means one step backwards. 



### Slice the String



txt = "Hello World"**[::-1]**
 print(txt)

Now we have a string `txt` that reads "Hello 
World" backwards.


Print the String to demonstrate the result



### Print the List



txt = "Hello World"[::-1]
**print(txt)**

