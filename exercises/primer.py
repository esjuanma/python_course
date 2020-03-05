# optional structure
# [[Nombre_Gasto, Monto], [Nombre_Gasto, Monto], ...]
# [['Luz', 100], ['Gas', 200]]

# Current structure
# ['Luz', 'Gas', ...]
# [100, 20, 30, ...]

# Muestra instrucciones al usuario

# Loop
# Cual es el gasto? [Gasto | No]
# Gasto != No? -> Cual es el monto? [Monto]

# Informe de resultados según información cargada
# Cada uno de los registros, con el porcentaje relativo total 10%
# Total $100


# Lista de gastos
servicesNames = []
servicesValues = []

# Variables para el loop
newRegistry = True
total = 0

# Loop para pedir gastos
while newRegistry:
    val = input("Si desea ingresar un gasto, ponga 'Si', sino 'No' ")
    val = val.lower()

    if val == 'si':
        # Gets service name
        serviceName = input('Ingrese el nombre del gasto: ')
                
        # Gets service value/cost
        serviceValue = input('Ingrese el monto del gasto: ')
        
        # Validates if is numeric
        if serviceValue.isnumeric():
            serviceValue = int(serviceValue)
            servicesValues.append(serviceValue)
        else:
            print('Ingrese un numero valido')
            continue

        servicesNames.append(serviceName)

        # Sums total
        total = total + serviceValue
    elif val == 'no':
        # breaks loop
        newRegistry = False
    else:
        # Shows instructions again to numb people
        print("Ingrese 'Si' o 'No'")

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



# - Luz: $100 (66%)
# - Gas: $50 (33%)
# -----------------
# Total $150

#print(servicesNames)
#print(servicesValues)