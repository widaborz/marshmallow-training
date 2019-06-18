from marshmallow import Schema, fields, pprint

class Person (object): 
    def __init__(self, name, age, address):
        self.name = name 
        self.age = age 
        self.address = address

    def __repr__(self):
        return '{} is {} years old'.format(self.name, self.age)

class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer()
    address = fields.String()

input_dict = {}

input_dict['name'] = input('What is your name? ')
input_dict['age'] = input('How old are you? ')
input_dict['address'] = input('What is your address? ')

person = Person(name=input_dict['name'], age=input_dict['age'], address=input_dict['address'])

#print(person)

schema = PersonSchema()

result = schema.dump(person)

pprint(result)

user_data = {'address': 'roma', 'age': 24, 'name': 'mario'}

mario_schema = PersonSchema()
result = mario_schema.load(user_data)
pprint(result)