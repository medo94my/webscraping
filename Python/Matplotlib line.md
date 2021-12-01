
Matplotlib Line
===============


Linestyle
---------


You can use the keyword argument `linestyle`, or shorter `ls`, to 
change the style of the plotted line:



### Example


Use a dotted line:



```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

```

### Result:



![](img_matplotlib_line_dotted.png)





### Example


Use a dashed line:



```python
plt.plot(ypoints, linestyle = 'dashed')


```

### Result:



![](img_matplotlib_line_dashed.png)




