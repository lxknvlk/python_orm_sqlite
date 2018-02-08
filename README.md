# python_orm_sqlite
A very simple python object oriented orm layer 

Each object has methods:
.create() .update() and .fetch()

To add a new field to a class:
1) add it to class, initialize.
2) add its name to fields array.
3)run python remake.py. 

Then you can create the object and set the new field an call .create() method and it will be persisted in the table with the newly added field. 

To update an object you have to set its idfield and additional fields, then call .update() on it.

To fetch an object you have to set its idfield and call .fetch()
