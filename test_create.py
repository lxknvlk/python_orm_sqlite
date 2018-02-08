from objects.user import User
from objects.location import Location

u = User()
u.username = "bob"
u.password = "123ss"
u.email = "bob@aooo.ooo"
u.ip = "123.123.123.123"
print u.create()

l = Location()
l.name = "City"
l.id = "[1,2,3]"
l.x = 1
l.y = 2
l.z = 3
l.description = "a small city near a river"
print l.create()
