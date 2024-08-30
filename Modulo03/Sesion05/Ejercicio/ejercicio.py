# Número del cual queremos calcular el factorial
numero = input("Ingrese un numero para calcular su factorial")

#Extraido de la documentacion de python
# El metodo isdigit() Devuelve True si todos los caracteres de la cadena son dígitos y hay al menos un carácter,
# Falso caso contrario.
if numero.isdigit():
    numero=int(numero)

    # calcular el factorial de un número, asignarlo a una variable,  
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    # y luego imprimirla.
    print(f"El factorial de {numero} es {factorial}")
else:
    print("Debe ingresar un entero positivo o un cero")