# Counter - Asks user for quantity of names to enter
numberOfNames = int(input('How many names do you know? '))

# Asks user for 3 different name
names = []

# Counter forwhile loop
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
while nameNumber < len(names):
    nameNumber = nameNumber + 1
    print('Name n', nameNumber, ':', names[nameNumber - 1])

# Immediate break!
while True:
    print('Only once!')
    break