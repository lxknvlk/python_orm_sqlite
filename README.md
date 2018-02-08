# python_orm_sqlite
A very simple python object oriented orm layer 

Each object has methods:
.create() .update() and .fetch()

To add a new field to a class just add it to the fields array in the class and specify its type. Then run python remake.py. Then you can create the object and set the new field an call .create() method and it will be persisted in the table with the newly added field. 

To update an object you have to set its idfield and additional fields, then call .update() on it.

To fetch an object you have to set its idfield and call .fetch()
