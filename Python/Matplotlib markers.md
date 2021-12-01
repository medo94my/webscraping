
Matplotlib Markers
==================


Markers
-------


You can use the keyword argument `marker` to 
emphasize each point with a specified marker:



### Example


Mark each point with a circle:



```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

```

### Result:



![](img_matplotlib_marker_o.png)





### Example


Mark each point with a star:



```python
...

plt.plot(ypoints, marker = '*')
...

```

### Result:



![](img_matplotlib_marker_star.png)




