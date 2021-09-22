from django.db import models

# Create your models here.
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

# Create your models here.


#class City(StructuredNode):
#    code = StringProperty(unique_index=True, required=True)
#    name = StringProperty(index=True, default="city")

class Person(StructuredNode):
    uid = UniqueIdProperty()
    id = StringProperty(unique_index=True)
    first_name = StringProperty(index=True)
    last_name = StringProperty(index=True)
    email = StringProperty(index=True)
    gender = StringProperty(index=True)
    address = StringProperty(index=True)
    phone = StringProperty(index=True)
    country = StringProperty(index=True)
    country_code = StringProperty(index=True)
    bank_id = StringProperty(index=True)
    is_pep = IntegerProperty(index=True, default=0)
    password = StringProperty(index=True)

#class User(StructuredNode):
#    username = StringProperty(index=True)
#    password = StringProperty(index=True)
#
#    # Relations :
#    city = RelationshipTo(City, 'LIVES_IN')
#    friends = RelationshipTo('Person','FRIEND')