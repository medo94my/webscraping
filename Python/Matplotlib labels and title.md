
Matplotlib Labels and Title
===========================


Create Labels for a Plot
------------------------


With Pyplot, you can use the `xlabel()` and `ylabel()` functions to set a label for the x- and y-axis.



### Example


Add labels to the x- and y-axis:



```python
import numpy as npimport matplotlib.pyplot as pltx = np.array([80, 
  85, 90, 95, 100, 105, 110, 115, 120, 125])y = np.array([240, 250, 260, 
  270, 280, 290, 300, 310, 320, 330])plt.plot(x, y)plt.xlabel("Average 
  Pulse")plt.ylabel("Calorie Burnage")plt.show()

```

### Result:


![](img_matplotlib_labels.png)



Create a Title for a Plot
-------------------------


With Pyplot, you can use the `title()` function to set a title for the plot.



### Example


Add a plot title and labels for the x- and y-axis:



```python
import numpy as npimport matplotlib.pyplot as pltx = np.array([80, 
  85, 90, 95, 100, 105, 110, 115, 120, 125])y = np.array([240, 250, 260, 
  270, 280, 290, 300, 310, 320, 330])plt.plot(x, y)plt.title("Sports Watch Data")plt.xlabel("Average 
  Pulse")plt.ylabel("Calorie Burnage")plt.show()

```

### Result:


![](img_matplotlib_title.png)



