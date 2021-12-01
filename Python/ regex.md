
Python RegEx
============


A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.


RegEx can be used to check if a string contains the specified search pattern.


RegEx Module
------------


Python has a built-in package called `re`, which can be used to work with 
Regular Expressions.


Import the `re` module:




```python
import re
```


RegEx in Python
---------------


When you have imported the `re` module, you 
can start using regular expressions:



### Example


Search the string to see if it starts with "The" and ends with "Spain":



```python
import 
    retxt = "The rain in Spain"x = re.search("^The.*Spain$", txt)
```


RegEx Functions
---------------


The `re` module offers a set of functions that allows 
us to search a string for a match:




| Function | Description |
| --- | --- |
| [findall](#findall) | Returns a list containing all matches |
| [search](#search) | Returns a [Match object](#matchobject) if there is a match anywhere in the string |
| [split](#split) | Returns a list where the string has been split at each match  |
| [sub](#sub) | Replaces one or many matches with a string |

