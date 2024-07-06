from models import Property
from models import User

john, jane, doe = User('John', '1234'), User(
    'Jane', '2222'), User('Doe', '1111')
p1, p2, p3 = Property("Valmiki Bhavan", 10), Property(
    "Shankar Bhavan", 20), Property("Vyas Bhavan", 15)

john.add_property(p1)
jane.add_property(p2)
doe.add_property(p3)


print("john : " , john.wealth)

users = [john, jane, doe]
properties = [p1, p2, p3]
