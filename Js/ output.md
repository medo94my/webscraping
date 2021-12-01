
JavaScript Output
=================


JavaScript Display Possibilities
--------------------------------


JavaScript can "display" data in different ways:


* Writing into an HTML element, using `innerHTML`.
* Writing into the HTML output using `document.write()`.
* Writing into an alert box, using `window.alert()`.
* Writing into the browser console, using `console.log()`.


Using innerHTML
---------------


To access an HTML element, JavaScript can use the `document.getElementById(id)` method. 


The `id` attribute defines the HTML element. The `innerHTML` property defines the HTML content:



### Example



```
<!DOCTYPE html><html>
<body>

<h1>My First Web Page</h1>
 <p>My First Paragraph</p>
<p id="demo"></p>

<script>
 document.getElementById("demo").innerHTML = 5 + 6;

    </script>

</body>
</html>

```



Changing the innerHTML property of an HTML element
is a common way to display data in HTML.



Using document.write()
----------------------


For testing purposes, it is convenient to use `document.write()`:



### Example



```
<!DOCTYPE html><html>
<body><h1>My First Web Page</h1>
 <p>My first paragraph.</p>
<script>document.write(5 + 6);
</script>

</body>
</html>

```



Using document.write() after an HTML document is loaded, will **delete all existing HTML**:




### Example



```
<!DOCTYPE html>
<html>
<body>
<h1>My First Web Page</h1>
 <p>My first paragraph.</p>
<button type="button" onclick="document.write(5 + 6)">Try it</button>
</body>
</html>

```



The document.write() method should only be used for testing.


