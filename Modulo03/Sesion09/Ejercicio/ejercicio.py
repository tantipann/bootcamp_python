def validar_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número positivo.")

def calcular_area_rectangulo(base,altura):
    area = base * altura
    print(f"El área del rectángulo es: {area}")


flag = True
while flag:
    base = validar_positivo("Introduce la base del rectángulo:  ")
    altura = validar_positivo("Introduce la altura del rectángulo:  ")
    calcular_area_rectangulo(base, altura)
    while True:
        respuesta = input("¿Desea calcular otra área? (Digite S para sí o N para salir): ").upper()
        if respuesta.upper() in ('N', 'S'):
            break
        else:
            print("Entrada no válida. Por favor, ingrese 'S' para sí o 'N' para salir.")

    if respuesta == 'N':
        flag = False
