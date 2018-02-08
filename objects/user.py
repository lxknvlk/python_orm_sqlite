from manager import update
from manager import fetch
from manager import create
from object import Object

class User(Object):
    table = "user"

    username = "" ##
    password = "" ##
    email = "" ##

    location = "" ##
    x = 0 ##
    y = 0 ##
    z = 0 ##

    socket = None
    server = 0
    ip = "" ##
    logged = 0 ##

    created = "" ##
    updated = "" ##

    def __str__(self):
        return self.username + "/" + self.password + "/" + self.email + "/" + self.ip

    def send(self, message):
        if self.socket:
            self.socket.send(message + "\n")
        return
