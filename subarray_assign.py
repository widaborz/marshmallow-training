from marshmallow import Schema, fields, pprint, post_load, ValidationError

data = {"subarrayID": 1, "dish": {"receptorIDList": ["0001", "0002"]}}


#dish class definition
class Dish(object):
    def __init__(self, receptorIDList): 
        self.receptorIDList = receptorIDList

    def __repr__(self): 
        idList = ""
        for receptorId in self.receptorIDList:
            idList = idList + " " + receptorId
        return '{}'.format(idList)

#subarray class definition
class SubArray(object):
    def __init__(self, subarrayID, dish):
        self.dish = dish
        self.subarrayID = subarrayID

    def __repr__(self):
        return 'SubArray {} is composed of receptorIDList {} '.format(self.subarrayID, self.dish)


#create dish and subarray objects
myDish = Dish(receptorIDList=["0003", "0004"])
mySubArray = SubArray(2, myDish)

print(myDish)

print(mySubArray)

#definition of Schema
class DishSchema(Schema): 
    receptorIDList = fields.List(fields.String()) #https://marshmallow.readthedocs.io/en/3.0/api_reference.html

    @post_load
    def create_Dish(self, data):
        return Dish(**data)

class SubArraySchema(Schema):
    subarrayID = fields.Integer()
    dish = fields.Nested(DishSchema) #https://marshmallow.readthedocs.io/en/3.0/nesting.html

    @post_load
    def create_sub_array(self, data):
        return SubArray(**data)

print("serialization Data/JSON")
#dump data
subarrayJson = SubArraySchema()
resultSubArray = subarrayJson.dump(mySubArray)

dishJson = DishSchema()
result = dishJson.dump(myDish)

pprint(resultSubArray)

#deserialization
print("deserialization from Json to Data")
dish_to_deserialize = {"receptorIDList": ["0001", "0002"]}

#creation dish objet from json
dishFromJson = DishSchema()
resultDishFromJson = dishFromJson.load(dish_to_deserialize)

subarrayFromJson = SubArraySchema()
resultSubArrayFromJson = subarrayFromJson.load(data)


pprint(resultSubArrayFromJson)