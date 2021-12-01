
Matplotlib Getting Started
==========================


Installation of Matplotlib
--------------------------


If you have [Python](/python/default.asp) and [PIP](python_pip.asp) already installed on a system, then installation of 
Matplotlib is very easy.


Install it using this command:




C:\Users\*Your Name*>pip install matplotlib

If this command fails, then use a python distribution that already has Matplotlib installed,  like Anaconda, Spyder etc.


Import Matplotlib
-----------------


Once Matplotlib is installed, import it in your applications by adding the
`import *module*` statement:




```python
import matplotlib

```


Now Matplotlib is imported and ready to use:


Checking Matplotlib Version
---------------------------


The version string is stored under `__version__` 
attribute.



### Example



```python
import matplotlibprint(matplotlib.\_\_version\_\_)

```



**Note:** two underscore characters are used in `__version__`.



