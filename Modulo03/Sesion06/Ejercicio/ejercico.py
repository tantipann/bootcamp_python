#Escribir un programa que analice un número
numero = input("Ingrese un número: ")

# Verificamos si la entrada es un número entero positivo o 
# negativo (especificamente si comienza con signo - y el resto del numero son digitos)
if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
    numero = float(numero) 
    
    #En caso de ser cero, también indicarlo
    if numero == 0:
        print("Número es cero")
    else:

        #Indique si es positivo o negativo
        if numero > 0:
            print("Número positivo")
        else:
            print("Número negativo")
        #si es par o impar
        if numero % 2 == 0:
                print("Número par")
        else:
            print("Número impar")
else:
    print("Debe ingresar un número válido")