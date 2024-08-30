# Lista de nombres
nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", 
    "Messi", "Teller", "Einstein", "Pele", "Juanes"
]

# Separar los nombres en tres grupos: magos, científicos y otros
#Y sabiendo que Harry Houdini, David Blaine y Teller son magos
magos = ["Harry Houdini", "David Blaine", "Teller"]

#Y también que Newton, Hawking y Einstein son científicos.
cientificos = ["Newton", "Hawking", "Einstein"]

#y otros
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

# escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
#frase ‘El gran‘ antes del nombre de cada mago.
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Imprimir en pantalla la lista completa de nombres antes de ser modificados;
print("Lista completa de nombres antes de ser modificados:")
imprimir_nombres(nombres)


# Hacer a los magos grandiosos
hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos
print("\nMagos grandiosos:")
imprimir_nombres(magos)

#los nombres de los científicos
print("\nCientíficos:")
imprimir_nombres(cientificos)

#y los restantes
print("\nOtros:")
imprimir_nombres(otros)
