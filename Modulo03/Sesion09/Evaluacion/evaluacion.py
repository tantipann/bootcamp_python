def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return "División por cero no permitida."

def operaciones(numero1, numero2):
    suma = sumar(numero1, numero2)
    resta = restar(numero1, numero2)
    multiplicacion = multiplicar(numero1, numero2)
    division = dividir(numero1, numero2)
    tupla=(suma, resta, multiplicacion, division)
    print(tupla)
    return tupla

def resultados_en_diccionario(numero1, numero2):
    suma, resta, multiplicacion, division = operaciones(numero1, numero2)
    resultados = {
        "Suma": suma,
        "Resta": resta,
        "Multiplicación": multiplicacion,
        "División": division
    }
    return resultados

def obtener_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Ingrese un numero valido")


primer_numero= 10
segundo_numero = 0
diccionario_resultados = resultados_en_diccionario(primer_numero, segundo_numero)
print("El diccinario de resultados es")
print(diccionario_resultados)

flag = True
while flag:
    primer_numero= obtener_numero("Introduce primer numero:  ")
    while True:
        segundo_numero= obtener_numero("Introduce segundo numero:  ")
        if segundo_numero != 0:
            break
        else:
            print("Ingrese un nuemro distinto de cero")
    diccionario_resultados = resultados_en_diccionario(primer_numero, segundo_numero)
    print("El diccinario de resultados es")
    print(diccionario_resultados)
    while True:
        respuesta = input("¿Desea ingresar otros numeros? (Digite S para sí o N para salir): ").upper()
        if respuesta.upper() in ('N', 'S'):
            break
        else:
            print("Entrada no válida. Por favor, ingrese 'S' para sí o 'N' para salir.")

    if respuesta == 'N':
        flag = False
