# Creates expected result message
message = 'El resultado debería ser 5.400.000'

# Creates a list of numbers
numbers = [10, 5, 80, 90, 15]

# Creates counter/pow
pow = 1

# Loops over list
for number in numbers:
    pow = pow * number

# Print message to the user
print(message, 'y da', pow) # 5.400.000

# Asks user for 3 different name
names = []
names.append(input('Decime un nombre'))
names.append(input('Decime otro nombre'))
names.append(input('El último'))

# Create counter for the loop
nameNumber = 0

# Shows names
for name in names:
    nameNumber = nameNumber + 1
    print('Name n', nameNumber, ':', name)