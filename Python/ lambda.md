
Python Lambda
=============


A lambda function is a small anonymous function.


A lambda function can take any number of arguments, but can only have one expression.


Syntax
------



lambda *arguments* : *expression*

The expression is executed and the result is returned:



### Example


Add 10 to argument `a`, and 
 return the result:



```python
x = lambda a : a + 10print(x(5))
```


Lambda functions can take any number of arguments:



### Example


Multiply argument `a` with argument 
 `b` and return the 
 result:



```python
x = lambda a, b : a * bprint(x(5, 6))
```



### Example


Summarize argument `a`, 
 `b`, and `c` and 
 return the 
 result:



```python
x = lambda a, b, c : a + b + cprint(x(5, 6, 
  2))
```

