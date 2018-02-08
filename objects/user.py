from manager import update
from manager import fetch
from manager import create

class User:
    table = "users"
    idfield = "username"
    fields = ["username VARCHAR PRIMARY KEY", "password VARCHAR", "email VARCHAR", "x INTEGER", "y INTEGER", "z INTEGER",
              "ip VARCHAR", "logged INTEGER", "created VARCHAR", "updated VARCHAR"]

    username = ""
    password = ""
    email = ""

    location = ""
    x = 0
    y = 0
    z = 0

    socket = None
    server = 0
    ip = ""
    logged = 0

    created = ""
    updated = ""

    def update(self):
        return update(self)

    def create(self):
        return create(self)

    def fetch(self):
        return fetch(self)

    def __str__(self):
        return self.username + "/" + self.password + "/" + self.email + "/" + self.ip

    def send(self, message):
        if self.socket:
            self.socket.send(message + "\n")
        return
