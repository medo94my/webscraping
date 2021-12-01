
Machine Learning - Scatter Plot
===============================


Scatter Plot
------------


A scatter plot is a diagram where each value in the data set is represented by a dot.


![](img_scatterplot.png)
The Matplotlib module has a method for drawing scatter plots, it needs two arrays of 
the same length, one for the values of the x-axis, and one for the values of the 
y-axis:



`x = [5,7,8,7,2,17,2,9,4,11,12,9,6]`


`y = [99,86,87,88,111,86,103,87,94,78,77,85,86]`



The `x` array represents the age of each car.


The `y` array represents the speed of each car.



### Example


Use the `scatter()` method to draw a scatter 
 plot diagram:



```python
import matplotlib.pyplot as pltx = 
  [5,7,8,7,2,17,2,9,4,11,12,9,6]y = 
  [99,86,87,88,111,86,103,87,94,78,77,85,86]plt.scatter(x, y)
  plt.show()

```

### Result:


![](img_matplotlib_scatter.png)



### Scatter Plot Explained


The x-axis represents ages, and the y-axis represents speeds.


What we can read from the diagram is that the two fastest cars were both 2 
years old, and the slowest car was 12 years old.



**Note:** It seems that the newer the car, the faster it 
 drives, but that could be a coincidence, after all we only registered 13 cars.



