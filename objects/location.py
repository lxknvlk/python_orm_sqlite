from manager import update
from manager import fetch
from manager import create
from object import Object

class Location(Object):
    table = "location"

    id = "" ##
    name = "" ##
    description = "" ##

    def __str__(self):
        return self.name + "/" + self.description