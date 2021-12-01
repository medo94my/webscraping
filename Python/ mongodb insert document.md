
Python MongoDB Insert Document
==============================



A **document** in MongoDB is the same as a **record** in SQL databases.



Insert Into Collection
----------------------


To insert a record, or *document* as it is called in MongoDB, into a collection, we use the 
`insert_one()` method.


The first parameter of the `insert_one()` method is a 
dictionary containing the 
name(s) and value(s) of each field in the document you want to insert.



### Example


Insert a record in the "customers" collection:



```python
import pymongomyclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["mydatabase"]mycol = mydb["customers"]
mydict = {
 "name": "John", "address": "Highway 37" }

  x =
  mycol.insert\_one(mydict)
```


Return the \_id Field
---------------------


The `insert_one()` method returns a InsertOneResult object, which has a 
property, `inserted_id`, that holds the id of the inserted document.



### Example


Insert another record in the "customers" collection, and return the value of the
`_id` field:



```python
mydict = {
 "name": "Peter", "address": "Lowstreet 27" }

  x = mycol.insert\_one(mydict)print(x.inserted\_id)
```


If you do not specify an `_id` field, then MongoDB 
will add one for you and assign a unique id for each document.


In the example above no `_id` field was 
specified, so MongoDB assigned a unique 
\_id for the record (document).


