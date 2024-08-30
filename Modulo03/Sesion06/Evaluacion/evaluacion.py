
# dados 3 números diferentes
numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")
numero3 = input("Ingrese el tercer número: ")

mayor = 0
medio = 0
menor = 0


# Verificar si todos los números son validos
es_numero1 = numero1.isdigit() or (numero1.startswith('-') and numero1[1:].isdigit())
es_numero2 = numero2.isdigit() or (numero2.startswith('-') and numero2[1:].isdigit())
es_numero3 = numero3.isdigit() or (numero3.startswith('-') and numero3[1:].isdigit())

# Da true si todos son numeros validos y false si al menos uno es invalido
solo_numeros = es_numero1 and es_numero2 and es_numero3


# Verificamos si la entrada es un número positivo o  negativo 
if solo_numeros == True:

    #los evalúe y entregue el orden de mayor a menor. usando if    
    if numero1 > numero2 and numero1 > numero3:
        mayor = numero1
        if numero2 > numero3:
            medio = numero2
            menor = numero3
        else:
            medio = numero3
            menor = numero2
    elif numero2 > numero1 and numero2 > numero3:
        mayor = numero2
        if numero1 > numero3:
            medio = numero1
            menor = numero3
        else:
            medio = numero3
            menor = numero1
    else:
        mayor = numero3
        if numero1 > numero2:
            medio = numero1
            menor = numero2
        else:
            medio = numero2
            menor = numero1

    #entregue el orden de mayor a menor.
    print(f"Los numeros ordenados de mayor a menor son : {mayor}, {medio} y {menor}")
else:
    print("Debe ingresar un solo numeros")
