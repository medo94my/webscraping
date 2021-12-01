
JavaScript Where To
===================


The <script> Tag
----------------


In HTML, JavaScript code is inserted between `<script>` and `</script>` tags.



### Example



<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>







Old JavaScript examples may use a type attribute: <script type="text/javascript">.
The type attribute is not required. JavaScript is the default scripting language in HTML.



JavaScript Functions and Events
-------------------------------


A JavaScript `function` is a block of JavaScript code, that can be executed when "called" for.



You will learn much more about functions and events in later chapters.



JavaScript in <head> or <body>
------------------------------


You can place any number of scripts in an HTML document.


Scripts can be placed in the `<body>`, or in the `<head>` section of an HTML page, or in both.


JavaScript in <head>
--------------------


In this example, a JavaScript `function` is placed in the `<head>` section 
of an HTML page.


The function is invoked (called) when a button is clicked:



### Example



<!DOCTYPE html>
<html>
<head>
<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
</script>
</head><body>
<h2>Demo JavaScript in Head</h2>

<p id="demo">A Paragraph</p><button type="button" onclick="myFunction()">Try 
it</button>


</body>
</html>




