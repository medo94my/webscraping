
Python File Open
================


Open a File on the Server
-------------------------


Assume we have the following file, located in the same folder as Python:



demofile.txt



 Hello! Welcome to demofile.txtThis file is for testing purposes.Good 
 Luck!

To open the file, use the built-in `open()` function.


The `open()` function returns a file object, which has a 
`read()` method for reading the content of the file:



### Example



```python
f = open("demofile.txt", "r")print(f.read())
```


If the file is located in a different location, you will have to specify the file path, 
like this:



### Example


Open a file on a different location:



```python
f = open("D:\\myfiles\welcome.txt", "r")print(f.read())
```


Read Only Parts of the File
---------------------------


By default the `read()` method returns the whole text, but you can also specify how many characters you want to return:



### Example


Return the 5 first characters of the file:



```python
f = open("demofile.txt", "r")print(f.read(5))
```


