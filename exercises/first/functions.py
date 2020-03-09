# Lista de gastos
servicesNames = []
servicesValues = []

def askToContinue():
    print('====================================================')
    val = input("Si desea ingresar un gasto, ponga 'Si', sino 'No' ")
    print('====================================================')
    return val.lower()

def askForExpenditures():
    # Variables para el loop
    newRegistry = True
    total = 0

    # Loop para pedir gastos
    while newRegistry:
        val = askToContinue()

        if val == 'si':
            # Gets service name
            serviceName = input('Ingrese el nombre del gasto: ')
                    
            # Gets service value/cost
            serviceValue = input('Ingrese el monto del gasto: ')
            
            # Validates if is numeric
            if not serviceValue.isnumeric():
                print('Ingrese un numero valido')
                continue

            # Converts to integer
            serviceValue = int(serviceValue)

            # Appends values
            servicesValues.append(serviceValue)
            servicesNames.append(serviceName)

            # Sums total
            total = total + serviceValue
        elif val == 'no':
            # breaks loop
            newRegistry = False
        else:
            # Shows instructions again to numb people
            print("Ingrese 'Si' o 'No'")

    return total

def printData(total):
    # Create counter for the loop
    nameNumber = 0

    # Shows names
    while nameNumber < len(servicesNames):
        # (costo de serv. / total) * 100 %
        percentage = int(servicesValues[nameNumber] / total * 100)
        
        message = 'El nombre del servicio es: '
        message += servicesNames[nameNumber]
        message += ' y cuesta: $'
        message += str(servicesValues[nameNumber])
        message += ' - ('
        message += str(percentage)
        message += '%)'

        print(message)

        # print('El nombre del servicio es:', servicesNames[nameNumber], 'y cuesta: $', , '- (', percentage, '%)')
        nameNumber = nameNumber + 1

def save(date):
    # Opens file and creates file variable
    with open('expenditures.txt', 'a') as file:
        # Create counter for the loop
        nameNumber = 0

        if date:
            file.write(date + '\n')

        # For each service
        while nameNumber < len(servicesNames):
            # Gets name and value
            serviceName = servicesNames[nameNumber]
            value = str(servicesValues[nameNumber])

            # Writes in file
            file.write(serviceName + ': $' + value + '\n')

            # Increases counter (avoids infinites loops and 50megas files)
            nameNumber += 1
        
        if date:
            file.write('\n')

# Read file and print current information
def read():
    print('Pendiente')