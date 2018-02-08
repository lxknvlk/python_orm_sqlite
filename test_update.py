from objects.user import User
from objects.location import Location

u = User()
u.username = "bob"
u.password = "ness"
u.email = "newehehe@aooo.com"
print u.update()

l = Location()
l.name = "Huge City"
l.id = "[1,2,3]"
l.x = 1
l.y = 2
l.z = 3
l.description = "a really big city"
print l.update()
