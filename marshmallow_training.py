from marshmallow import Schema, fields, pprint, post_load

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

    @post_load
    def create_person(self, data):
        return Person(**data)


#input_dict = {}

#input_dict['name'] = input('What is your name? ')
#input_dict['age'] = input('How old are you? ')
#input_dict['address'] = input('What is your address? ')

#matteo = Person(name=input_dict['name'], age=input_dict['age'], address=input_dict['address'])

matteo = Person(name = 'matteo', address = 'sanzio', age = 34)
mario = Person(name = 'mario', address = 'roma', age = 19) 

utenti_result = PersonSchema(many=True)
result = utenti_result.dump([matteo, mario])
pprint(result)