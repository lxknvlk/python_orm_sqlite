from manager import update
from manager import fetch
from manager import create
from object import Object

class Location(Object):
    table = "locations"
    idfield = "id"
    fields = ["id VARCHAR PRIMARY KEY", "name VARCHAR", "x INTEGER", "y INTEGER", "z INTEGER", "description VARCHAR"]

    id = ""
    name = ""
    x = 0
    y = 0
    z = 0
    description = ""

    def __str__(self):
        return self.name + "/" + self.description