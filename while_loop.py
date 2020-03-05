# Counter - Asks user for quantity of names to enter
numberOfNames = int(input('How many names do you know? '))

# Asks user for 3 different name
names = []

# Counter for while loop
count = 1

# Loops while
while count <= numberOfNames:
    newName = input('Give me the name ')
    names.append(newName)
    count = count + 1

    if count > numberOfNames:
        break
else:
    print('You know nothin, Jon Snow')

# Create counter for the loop
nameNumber = 0

# Shows names
for name in names:
    nameNumber = nameNumber + 1
    print('Name n', nameNumber, ':', name)
