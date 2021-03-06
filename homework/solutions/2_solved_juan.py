# 1
# Crear un archivo vacío llamado "pow.txt" en el mismo directorio del script (se puede crear de forma "manual")
# Crear una función en Python que a cada ejecución:
# - Abra el archivo
# -- Si el archivo está vacío, escribe un número aleatorio entre 2 y 9 (*) y finaliza el script
# -- Caso contrario, guarda en memoria el primer y último número encontrado en el archivo,
# -- y luego escribe, al final del mismo, el producto de ambos números. Finaliza el script.

# AYUDA
# Revisar exercises/first/expenditures/functions.py para ver manejo de archivos
# Para abrir un archivo con VSCode, apretar Ctrl+P y escribir el nombre del archivo
# (*) https://www.programiz.com/python-programming/examples/random-number

#########################################
# Solución basada en la solución de Bri #
#########################################

import random

config = {
    'file_route': '.\homework\solutions\pow.txt'
}

def addPow():
    # Creates file
    archivoEscritura = open(config['file_route'], 'a')
    archivoLectura = open(config['file_route'])

    # Creates variables for saving first and last value from file
    firstVal = None
    lastVal = None

    # Reads each line in file
    for line in archivoLectura:
        # Convert line to integer
        line = int(line)

        # Gets first value
        if firstVal == None:
            firstVal = line

        # Updates last value
        lastVal = line

    # Writes a random number if counter is equals to 0
    if firstVal == None:
        firstVal = 1
        lastVal = random.randint(0, 9)

    # New line with number
    newLine = str(firstVal * lastVal) + '\n'

    # Write!
    archivoEscritura.write(newLine)

addPow()
