# Creates a list of numbers
numbers = [10, 5, 80, 90, 15]

# Creates counter/pow
pow = 1

with open('expenditures.txt', 'a') as file:
    # Loops over list
    for number in numbers:
        pow = pow * number
        file.write(str(pow * number) + '\n')

file = open('expenditures.txt')

for line in file:
    print(line)

file.close()
