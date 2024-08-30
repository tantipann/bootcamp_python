#Requerimos eliminar todas las vocales de la palabra “paralelepípedo”
palabra = "paralelepípedo"
# Lista de vocales a eliminar tanto mayusculas como minusculas
vocales = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

# lista para almacenar las consonantes y su posicion
consonantes_posicion = []

posicion = 1

# Iterar sobre cada carácter en la palabra
for caracter in palabra:

    if caracter not in vocales:
        #Si el caracter no se encuentra en la lista de vocales se agrega la tupla
        #caracter-posicion a la lista de comsonantes
        consonantes_posicion.append((caracter, posicion))
    posicion += 1  


contador = 0 
while contador < len(consonantes_posicion):
    #Como consonantes_posicion esta compuesta por tuplas se le asigna el primes valor consonantes
    # y el segundo valor a posicion
    consonante, posicion = consonantes_posicion[contador]
    # imprimir en pantalla las consonantes restantes y su posición dentro de dicha palabra.
    print(f"Consonante: {consonante}, Posición: {posicion}")
    contador += 1  