# Creates initial variables values
bodyTemperature = 39.5
difficultyBreathing = False
diabetes = True
cancer = False
isPregnant = False
isOver60yearOld = False
hepatic = False
kidneyDisease = False
respiratoryDisease = False

# Version 2
if (bodyTemperature >= 38 and 
    (difficultyBreathing or
    diabetes or
    cancer or
    isPregnant or
    isOver60yearOld or
    hepatic or
    kidneyDisease or
    respiratoryDisease)):
    # Prints te vas a morir de coronita
    print('Tiene un factor de riesgo')
elif bodyTemperature >= 38:
    # Prints tiene fiebre
    print('Tiene fiebre')
else:
    # Prints ta todo bien
    print('Diagnostico bueno')

"""
# Version 1
if bodyTemperature >= 38:
    if (difficultyBreathing or
        diabetes or
        cancer or
        isPregnant or
        isOver60yearOld or
        hepatic or
        kidneyDisease or
        respiratoryDisease):
        # Prints te vas a morir de coronita
        print('Tiene coronita')
    else:
        # Prints tiene fiebre
        print('Tiene fiebre')
else:
    # Prints ta todo bien
    print('Diagnostico bueno')
"""