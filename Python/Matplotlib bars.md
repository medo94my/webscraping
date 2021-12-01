
Matplotlib Bars
===============


Creating Bars
-------------


With Pyplot, you can use the `bar()` function 
to draw bar graphs:



### Example


Draw 4 bars:



```python
import matplotlib.pyplot as pltimport numpy as npx = np.array(["A", 
  "B", "C", "D"])y = np.array([3, 8, 1, 10])plt.bar(x,y)plt.show()

```

### Result:



![](img_matplotlib_bars1.png)




The `bar()` function takes arguments that describes the 
layout of the bars.


The categories and their values represented by the *first*and *second* argument as arrays.



### Example



```python
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)

```






