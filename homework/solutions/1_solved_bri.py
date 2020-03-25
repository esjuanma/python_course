def sum():
    # 1
    # Pedir números al usuario de forma indefinida e imprimir la suma al final
    # para cortar con el pedido de números, utiilzar algún caracter o valor específico

    # Create boolean for loop and int for sum
    sumar = True
    total = 0

    # Loop for asking numbers & sum total - it will end when entering a '0'
    while sumar == True:
        numero = int(input ('Ingrese un numero, si desea finalizar, ingrese un 0: '))
        if numero == 0:
            sumar = False
        else:
            total = total + numero

    # Shows total
    print ('La suma de los numeros ingresados es:', total)

def tables():
    # 2
    # Crear función que devuelve las tablas del número 1 al 10
    # ej: [[1,2,3,4,5,6,...,10], ..., [10,20,30,...]]

    # Create list of numbers to multiply, list for showing the tables & counter for loop
    numeros = [1,2,3,4,5,6,7,8,9,10]
    tablas = []
    contador = 0

    # Loop for multiplying the numbers
    #for numero in numeros:
    #    contador = contador + 1
    #    tablas.append([contador*1,contador*2,contador*3,contador*4,contador*5,contador*6,contador*7,contador*8,contador*9,contador*10,])

    for numero in numeros:
        contador +=1
        auxiliar = []
        for n in range(10):
            auxiliar.append(numero*(n+1))
        tablas.append(auxiliar)    


    # Shows tables
    print ('Las tablas del 1 al 10 son:\n', tablas)

def palindromic():
    # 3
    # Pedir al usuario un texto (una o varias palabras) y indicar si es capicua. Case-insensitive.

    # Asks user to enter a text or word
    original = input('Ingrese una palabra u oracion para verificar si es capicua: \n')

    # Converts the text to lowercase
    original = original.lower().replace(' ', '')

    # Creates a variable inverted from original
    capicua = original[::-1]

    # Compares if original is equal to capicua and shows the result
    if original == capicua:
        #print ('El texto ingresado es capicua:\n', original.replace(' ', ''), '\n', capicua.replace(' ', ''))
        print ('El texto ingresado es capicua')
    else:
        print ('El texto ingresado no es capicua')




# 4
# Pedir un número natural al usuario e indicar si es primo. 1 no es primo.

def primeNumbers():
    # Asks user to enter a number
    numero = int(input ('Ingrese un numero para verificar si es primo o no: \n'))

    # Creates counter & boolean for loop
    comparar = 2
    EsPrimo = True

    # Loop for checking if there is one more number that can divide the user's number
    while comparar < numero and EsPrimo == True:
        if numero%comparar == 0:
            EsPrimo = False
            print ('El numero', numero, 'es divisible por', comparar)
        else:
            comparar = comparar + 1

    # Shows result
    if EsPrimo == True and numero != 1:
        print ('El numero', numero, 'es primo')
    else:
        print ('El numero', numero, 'no es primo')


