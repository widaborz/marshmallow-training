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
        return 'SubArray {} is composed of dishIdList {}'.format(self.subarrayID, self.dish)

#dish class definition
class Dish(object):
    def __init__(self, receptorIDList): 
        self.receptorIDList = receptorIDList

    def __repr__(self): 
        return 'Dish has {} receptorIDList'.format(self.receptorIDList)

#create dish and subarray objects
myDish = Dish(receptorIDList=["0001", "0002"])
mySubArray = SubArray(1, myDish)

print(myDish)

print(mySubArray)

#definition of Schema
class SubArraySchema(Schema):
    dish = fields.String()
    subarrayID = fields.String()

class DishSchema(Schema): 
    receptorIDList = fields.String()

#dump data
subarrayJson = SubArraySchema()
resultSubArray = subarrayJson.dump(mySubArray)

dishJson = DishSchema()
result = dishJson.dump(myDish)
pprint(result)

pprint(resultSubArray)


