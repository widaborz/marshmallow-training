from marshmallow import Schema, fields, pprint, post_load, ValidationError

data = {
            "subarrayID": 1, 
            "dish": {
                "receptorIDList": ["0001", "0002"]
            }
        }
#subarray class definition
class SubArray(object):
    def __init__(self, dish, subarrayID):
        self.dish = dish
        self.subarrayID = subarrayID

    def __repr__(self):
        return 'SubArray {} is composed of receptorIDList {}'.format(self.subarrayID, self.dish)

#dish class definition
class Dish(object):
    def __init__(self, receptorIDList): 
        self.receptorIDList = receptorIDList

    def __repr__(self): 
        idList = ""
        for receptorId in self.receptorIDList:
            idList = idList + " " + receptorId
        return 'Dish has {} receptorIDList'.format(idList)

#create dish and subarray objects
myDish = Dish(receptorIDList=["0003", "0004"])
mySubArray = SubArray(2, myDish)

print(myDish)

print(mySubArray)

#definition of Schema
class DishSchema(Schema): 
    receptorIDList = fields.List(fields.String()) #https://marshmallow.readthedocs.io/en/3.0/api_reference.html

class SubArraySchema(Schema):
    dish = fields.String()
    subarrayID = fields.Nested(DishSchema) #https://marshmallow.readthedocs.io/en/3.0/nesting.html

print("serialization Data/JSON")
#dump data
subarrayJson = SubArraySchema()
resultSubArray = subarrayJson.dump(mySubArray)

dishJson = DishSchema()
result = dishJson.dump(myDish)

pprint(resultSubArray)


