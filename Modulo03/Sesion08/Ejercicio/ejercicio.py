mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# 1. Eliminar los elementos duplicados.
sin_duplicados = set(mi_lista)
lista_ordenada = list(sin_duplicados)

# 2. Ordenar la lista resultante en orden ascendente
lista_ordenada.sort()

# Mostrar lista ordenada 
print("Lista sin duplicados y ordenada:", lista_ordenada)
