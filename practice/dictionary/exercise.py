person = {
    'name': 'Dan',
    'age': 35,
    "location": 'Seoul',
    'skills': ['Python', 'Javascript', 'react']
}


name = person['name']
location = person['location']

# OR

name2 = person.get('get')
happy = person.get('happiness')

person['email'] = 'danchin327@gmail.com'
person['mood'] = 'could be worse. Could be a whole lot better too.'
print(person)
del person['mood']

print(person)
