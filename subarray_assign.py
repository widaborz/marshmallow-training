from marshmallow import Schema, fields, pprint, post_load, ValidationError

data = {
            "subarrayID": 1, 
            "dish": {
                "receptorIDList": ["0001", "0002"]
            }
        }

class SubArray(object):
    def __init__(self, dish, subarrayID):
        self.dish = dish
        self.subarrayID = subarrayID

    def __repr__(self):
        return 'SubArray {} is composed of dishIdList {}'.format(self.subarrayID, self.dish)

class Dish(object):
    def __init__(self, receptorIDList): 
        self.receptorIDList = receptorIDList

    def __repr__(self): 
        return 'Dish has {} receptorIDList'.format(self.receptorIDList)


myDish = Dish(receptorIDList='1, 2')
mySubArray = SubArray(1, myDish)

print(myDish)

print(mySubArray)

