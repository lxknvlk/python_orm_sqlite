from objects.user import User
from objects.location import Location

u = User()
u.username = "bob"
print u.fetch()

# l = Location()
# l.id = "[1,2,3]"
# print l.fetch()