from manager import update
from manager import fetch
from manager import create

class Location:
    table = "locations"
    idfield = "id"
    fields = ["id VARCHAR", "name VARCHAR", "x INTEGER", "y INTEGER", "z INTEGER", "description VARCHAR"]

    id = ""
    name = ""
    x = 0
    y = 0
    z = 0
    description = ""

    def update(self):
        return update(self)

    def create(self):
        return create(self)

    def fetch(self):
        return fetch(self)

    def __str__(self):
        return self.name + "/" + self.description