# Ejemplos de uso de condicionales en pycharm# #Condicional elif#

edad = int(input("Ingrese la edad de la persona: \n"))

if (edad <=17):
    print('La persona aun no tiene edad necesaria para conducir.')

elif(edad <= 70):
    print("La persona esta autorizada para recibir su licencia de conducir.")
else:
    print('La persona necesita una licencia especial.')

