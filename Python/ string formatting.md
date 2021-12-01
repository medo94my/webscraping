
Python String Formatting
========================


To make sure a string will display as expected, we can format the result with 
the `format()` method.


String format()
---------------


The `format()` method allows you to format selected parts of a string.


Sometimes there are parts of a text that you do not control, maybe 
they come from a database, or user input?


To control such values, 
add placeholders (curly brackets `{}`) in the text, and run the values through the 
`format()` method:



### Example


Add a placeholder where you want to display the price:



```python
price = 49txt = "The price is {
}
 dollars"print(txt.format(price))

```


You can add parameters inside the curly brackets to specify how to convert 
the value:



### Example


Format the price to be displayed as a number with two decimals:



```python
txt = "The price is {
:.2f}
 dollars"

```


Check out all formatting types in our [String format() Reference](ref_string_format.asp).


Multiple Values
---------------


If you want to use more values, just add more values to the format() method:




```python
print(txt.format(price, itemno, count))

```


And add more placeholders:



### Example



```python
quantity = 3itemno = 567price = 49myorder = "I want {
}
 pieces of 
  item number {
}
 for {
:.2f}
 dollars."print(myorder.format(quantity, itemno, price))

```


Index Numbers
-------------


You can use index numbers (a number inside the curly brackets `{0}`) to be sure the 
values are placed 
in the correct placeholders:



### Example



```python
quantity = 3itemno = 567price = 49myorder = "I want {
0}
 pieces of 
  item number {
1}
 for {
2:.2f}
 dollars."print(myorder.format(quantity, itemno, price))

```


Also, if you want to refer to the same value more than once, use the index number:



### Example



```python
age = 36name = "John"txt = "His name is {
1}
. {
1}
 is {
0}
 years old."print(txt.format(age, 
  name))

```


Named Indexes
-------------


You can also use named indexes by entering a name inside the curly brackets `{carname}`, 
but then you must use names when you pass the parameter values
`txt.format(carname = "Ford")`:



### Example



```python
myorder = "I have a {
carname}
, it is a {
model}
."print(myorder.format(carname 
  = "Ford", model = "Mustang"))

```


