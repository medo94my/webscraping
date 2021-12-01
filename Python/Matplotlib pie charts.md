
Matplotlib Pie Charts
=====================


Creating Pie Charts
-------------------


With Pyplot, you can use the `pie()` function 
to draw pie charts:



### Example


A simple pie chart:



```python
import matplotlib.pyplot as pltimport numpy as npy = np.array([35, 
  25, 25, 15])plt.pie(y)plt.show() 

```

### Result:



![](img_matplotlib_pie1.png)




As you can see the pie chart draws one piece (called a wedge) for each value 
in the array (in this case [35, 25, 25, 15]).


By default the plotting of the first wedge starts from the x-axis and move *counterclockwise*:



![](img_matplotlib_pie_start.png)




**Note:** The size of each wedge is determined by comparing the value with all the other values, by using this formula:


The value divided by the sum of all values: `x/sum(x)`



