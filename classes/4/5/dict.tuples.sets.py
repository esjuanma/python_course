students = [{
    'firstname': 'Jon',
    'lastname': 'Snow',
    'skills': 'Knowing nothing'
}, {
    'firstname': 'Arya',
    'lastname': 'Stark',
    'skills': 'Killing people'
}]

store = {
    'address': '',
    'timetable': '...'
}

store.get('phone')

print(students)

my_dict = {
    'name': 'Jack',
    'age': 26
}

# Output: Jack
#print(my_dict.name)
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

print(({}).get('name', 'Qué hacés'))

otraTupla = ('01818321845', 'Alberto', 'Perez')

# objects
losLocos = {
    otraTupla: 'Más info de Alberto'
}

print(losLocos[otraTupla])

myTupla = (1, 2)
myTupla = (myTupla, (3, 4))