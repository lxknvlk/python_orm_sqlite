# python_orm_sqlite
A very simple python object oriented orm layer 

Each object has methods:
.create() .update() and .fetch()

To add a new field to a class:
1) add it to class, initialize with needed type like this
```
    location = "" ##
    x = 0 ##
```

2) add ## after the field, this indicates that field is persistable
3) first field that has ## will be primary key
4) run python remake.py. 

To add a new class:
1) create name.py class file in objects/ folder
2) add a field table that is the same as file name without extension
3) add fields, initialize them and put ## after
4) run python remake.py 

Then you can create the object and set the new field an call .create() method and it will be persisted in the table with the newly added field like this:
```
u = User()
u.username = "bob"
u.password = "123ss"
u.email = "bob@aooo.ooo"
u.ip = "123.123.123.123"
print u.create()
```

To update an object you have to set its idfield and additional fields, then call .update() on it.

```
u = User()
u.username = "bob"
u.password = "ness"
u.email = "newehehe@aooo.com"
print u.update()
```
new values will be saved to object with username "bob"

To fetch an object you have to set its idfield and call .fetch()

```
u = User()
u.username = "bob"
print u.fetch()
print u.email
```

user will be searched by username and full object will be returned
