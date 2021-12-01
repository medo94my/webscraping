
Matplotlib Plotting
===================


Plotting x and y points
-----------------------


The `plot()` function is used to draw points (markers) in a diagram.


By default, the `plot()` function draws a line from point to point.


The function takes parameters for specifying points in the diagram.


Parameter 1 is an array containing the points on the **x-axis**.


Parameter 2 is an array containing the points on the **y-axis**.


If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.



### Example


Draw a line in a diagram from position (1, 3) to position (8, 10):



```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

```

### Result:



![](img_matplotlib_plotting1.png)





The **x-axis** is the horizontal axis.


The **y-axis** is the vertical axis.



