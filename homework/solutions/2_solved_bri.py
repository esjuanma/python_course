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

import random

# Creates file
archivoEscritura = open('.\homework\solutions\pow.txt', 'a')
archivoLectura = open('.\homework\solutions\pow.txt')
# Creates counter for loop
contador = 0

# Creates variables for saving first and last value from file
firstVal = None
lastVal = None

# Reads each line in file
for line in archivoLectura:
    # Increases counter
    contador = contador + 1
    # Convert line to integer
    line = int(line)
    if contador == 1:
        firstVal = line
    else:
        lastVal = line

# Writes a random number if counter is equals to 0
if contador == 0: 
    number = random.randint(0,9)
    archivoEscritura.write(str(number) + '\n')
else:
    # Creates first pow
    if contador == 1:
        potencia = firstVal * firstVal
    # Creates last pow
    if contador > 1:
        potencia = firstVal * lastVal
    # Writes pow in file
    archivoEscritura.write(str(potencia) + '\n')