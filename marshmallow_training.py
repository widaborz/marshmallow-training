from marshmallow import Schema, fields, pprint, post_load, ValidationError


def validate_young(n): 
    if n<18: 
        raise ValidationError('Age must be more than 18')
    if n>50: 
        raise ValidationError('The user must be young')


class Person (object): 
    def __init__(self, name, age, address, email):
        self.name = name 
        self.age = age 
        self.address = address
        self.email = email

    def __repr__(self):
        return '{} is {} years old'.format(self.name, self.age)

class PersonSchema(Schema):
    name = fields.String()
    age = fields.Integer(validate = validate_young)
    address = fields.String()
    email = fields.Email()

    @post_load
    def create_person(self, data):
        return Person(**data)

def validate_young(n): 
    if n<18: 
        raise ValidationError('Age must be more than 18')
    if n>50: 
        raise ValidationError('The user must be young')


#input_dict = {}

#input_dict['name'] = input('What is your name? ')
#input_dict['age'] = input('How old are you? ')
#input_dict['address'] = input('What is your address? ')

#matteo = Person(name=input_dict['name'], age=input_dict['age'], address=input_dict['address'])

matteo = Person(name = 'matteo', address = 'sanzio', age = 34, email = '')
mario = Person(name = 'mario', address = 'roma', age = 19, email = '') 

utenti_result = PersonSchema(many=True)
result = utenti_result.dump([matteo, mario])
pprint(result)


print('dump data')

user_data = {'address': 'Via R. Sanzio, 24', 'age': 6, 'email': '', 'name': 'Matteo Canzari', 'email': 'matteo.canzari@gmail.com'}

load_data = PersonSchema()


try:
    result = load_data.load(user_data)
    print(result)
except ValidationError as err: 
    print('wrog mail address')
    print(err.message)


