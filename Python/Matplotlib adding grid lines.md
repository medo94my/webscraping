
Matplotlib Adding Grid Lines
============================


Add Grid Lines to a Plot
------------------------


With Pyplot, you can use the `grid()` function to add grid lines to the plot.



### Example


Add grid lines to the plot:



```python
import numpy as npimport matplotlib.pyplot as pltx = np.array([80, 
  85, 90, 95, 100, 105, 110, 115, 120, 125])y = np.array([240, 250, 260, 
  270, 280, 290, 300, 310, 320, 330])plt.title("Sports Watch Data")
  plt.xlabel("Average Pulse")plt.ylabel("Calorie Burnage")plt.plot(x, 
  y)plt.grid()plt.show() 
```

### Result:


![](img_matplotlib_grid.png)



