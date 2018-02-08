from manager import update
from manager import fetch
from manager import create
from object import Object

class Location(Object):
    table = "locations"
    idfield = "id"
    fields = ["id VARCHAR PRIMARY KEY", "name VARCHAR", "description VARCHAR"]

    id = ""
    name = ""
    description = ""

    def __str__(self):
        return self.name + "/" + self.description