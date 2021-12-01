
Machine Learning - Mean Median Mode
===================================


Mean, Median, and Mode
----------------------


What can we learn from looking at a group of numbers?


In Machine Learning (and in mathematics) there are often three values that 
interests us:


* **Mean** - The average value
* **Median** - The mid point value
* **Mode** - The most common value


Example: We have registered the speed of 13 cars:



`speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]`



What is the average, the middle, or the most common speed value?


Mean
----


The mean value is the average value.


To calculate the mean, find the sum of all values, and divide the sum by the number of values:



`(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 
 89.77`



The NumPy module has a method for this. Learn about the NumPy module in our [NumPy Tutorial](numpy/default.asp).



### Example


Use the NumPy `mean()` method to find the 
average speed:



```python
import numpyspeed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)print(x)
```


