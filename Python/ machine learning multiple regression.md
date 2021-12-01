
Machine Learning - Multiple Regression
======================================


Multiple Regression
-------------------


Multiple regression is like [linear regression](python_ml_linear_regression.asp), but with more than one 
independent value, meaning that we try to predict a value based on **two 
or more** variables.


Take a look at the data set below, it contains some information about cars.





| Car | Model | Volume | Weight | CO2 |  |





|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Toyota | Aygo | 1000 | 790 | 99 |
| Mitsubishi | Space Star | 1200 | 1160 | 95 |
| Skoda | Citigo | 1000 | 929 | 95 |
| Fiat | 500 | 900 | 865 | 90 |
| Mini | Cooper | 1500 | 1140 | 105 |
| VW | Up! | 1000 | 929 | 105 |
| Skoda | Fabia | 1400 | 1109 | 90 |
| Mercedes | A-Class | 1500 | 1365 | 92 |
| Ford | Fiesta | 1500 | 1112 | 98 |
| Audi | A1 | 1600 | 1150 | 99 |
| Hyundai | I20 | 1100 | 980 | 99 |
| Suzuki | Swift | 1300 | 990 | 101 |
| Ford | Fiesta | 1000 | 1112 | 99 |
| Honda | Civic | 1600 | 1252 | 94 |
| Hundai | I30 | 1600 | 1326 | 97 |
| Opel | Astra | 1600 | 1330 | 97 |
| BMW | 1 | 1600 | 1365 | 99 |
| Mazda | 3 | 2200 | 1280 | 104 |
| Skoda | Rapid | 1600 | 1119 | 104 |
| Ford | Focus | 2000 | 1328 | 105 |
| Ford | Mondeo | 1600 | 1584 | 94 |
| Opel | Insignia | 2000 | 1428 | 99 |
| Mercedes | C-Class | 2100 | 1365 | 99 |
| Skoda | Octavia | 1600 | 1415 | 99 |
| Volvo | S60 | 2000 | 1415 | 99 |
| Mercedes | CLA | 1500 | 1465 | 102 |
| Audi | A4 | 2000 | 1490 | 104 |
| Audi | A6 | 2000 | 1725 | 114 |
| Volvo | V70 | 1600 | 1523 | 109 |
| BMW | 5 | 2000 | 1705 | 114 |
| Mercedes | E-Class | 2100 | 1605 | 115 |
| Volvo | XC70 | 2000 | 1746 | 117 |
| Ford | B-Max | 1600 | 1235 | 104 |
| BMW | 2 | 1600 | 1390 | 108 |
| Opel | Zafira | 1600 | 1405 | 109 |
| Mercedes | SLK | 2500 | 1395 | 120 |




We can predict the CO2 emission of a car based on 
the size of the engine, but with multiple regression we can throw in more 
variables, like the weight of the car, to make the prediction more accurate.


How Does it Work?
-----------------


In Python we have modules that will do the work for us. Start by importing 
the Pandas module.



`import pandas`



Learn about the Pandas module in our [Pandas Tutorial](pandas_tutorial.asp).


The Pandas module allows us to read csv files and return a DataFrame object.


The file is meant for testing purposes only, you can download it here: <cars.csv>



`df = pandas.read_csv("cars.csv")`



Then make a list of the independent values and call this 
variable `X`. 


Put the dependent values in a variable called `y`.



`X = df[['Weight', 'Volume']]
y = df['CO2']`




**Tip:** It is common to name the list of independent values with a upper 
case X, and the list of dependent values with a lower case y.



We will use some methods from the sklearn module, so we will have to import that module as well:



`from sklearn import linear_model`



From the sklearn module we will use the `LinearRegression()` method 
to create a linear regression object.


This object has a method called `fit()` that takes 
the independent and dependent values as parameters and fills the regression object with data that describes the relationship:



`regr = linear_model.LinearRegression()
regr.fit(X, y)`



Now we have a regression object that are ready to predict CO2 values based on 
a car's weight and volume:



`#predict the CO2 emission of a car where the weight 
 is 2300kg, and the volume is 1300cm3:
 predictedCO2 = regr.predict([[2300, 1300]])`




### Example


See the whole example in action:



```python
import pandasfrom sklearn import linear\_modeldf = pandas.read\_csv("cars.csv")
X = df[['Weight', 'Volume']]y = df['CO2']regr = 
  linear\_model.LinearRegression()regr.fit(X, y)#predict the CO2 
  emission of a car where the weight is 2300kg, and the volume is 1300cm3:
  predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
```

### Result:




```python
[107.2087328]
```







We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, will release approximately 107 grams of CO2 for every 
kilometer it drives.


