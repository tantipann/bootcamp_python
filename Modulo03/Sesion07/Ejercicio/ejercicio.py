#Crear una lista con 10 números enteros
lista = [5,79,7,54,23,45,2,34,-2,0]

#recorrerla haciendo uso de la sentencia for
for numero in lista:
    #imprimir en pantalla el valor de cada elemento
    print(f"El numero es {numero} ")
    if numero == 0:
        #o cero
        print("Numero es cero\n")
    elif numero % 2 == 0:
        #indicando si es par
        print("Numero par\n")
    else:
        #impar
        print("Numero Impar\n")