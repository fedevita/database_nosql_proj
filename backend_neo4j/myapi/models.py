from django.db import models

# Create your models here.
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

# Create your models here.


class City(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    name = StringProperty(index=True, default="city")

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

class User(StructuredNode):
    username = StringProperty(index=True)
    password = StringProperty(index=True)

    # Relations :
    city = RelationshipTo(City, 'LIVES_IN')
    friends = RelationshipTo('Person','FRIEND')