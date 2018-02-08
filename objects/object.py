from manager import update
from manager import fetch
from manager import create

class Object:

    def update(self):
        return update(self)

    def create(self):
        return create(self)

    def fetch(self):
        return fetch(self)
