#Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
#[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

#Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
#segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
claves = ['A', 'B', 'C', 'D']

# Creación del diccionario resultante
diccionario = {}

#Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
for indice, sublista in enumerate(listas):
    #Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
    if sublista[0] == 0:
        continue

    #Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
    sublista_filtrada = []
    for numero in sublista:
        if numero != 0:
            sublista_filtrada.append(numero)

    # Asignacion de la sublista al diccionario
    diccionario[claves[indice]] = sublista_filtrada

    # Impresión de la sublista filtrada
    print(f"{claves[indice]}: {sublista_filtrada}")

#Finalmente, imprimiremos en pantalla el diccionario resultante.
print("\nDiccionario resultante:")
print(diccionario)