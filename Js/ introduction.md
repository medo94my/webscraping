
JavaScript Introduction
=======================



This page contains some examples of what JavaScript can do.



JavaScript Can Change HTML Content
----------------------------------


One of many JavaScript HTML methods is `getElementById()`.


The example below "finds" an HTML element (with id="demo"), 
and changes the element content (innerHTML) to "Hello JavaScript":



### Example



```
document.getElementById("demo").innerHTML = "Hello JavaScript";

```



JavaScript accepts both double and single quotes:




### Example



```
document.getElementById('demo').innerHTML = 'Hello JavaScript';

```


JavaScript Can Change HTML Attribute Values
-------------------------------------------


In this example JavaScript changes the value of the `src` (source) attribute of an `<img>` tag:



### The Light Bulb



![](pic_bulboff.gif)






