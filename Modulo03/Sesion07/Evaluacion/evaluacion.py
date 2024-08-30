# Lista de estudiantes

estudiantes = [
 {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
 {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
 {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
 {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
 ]

#Recorro la lista
for estudiante in estudiantes:
    edad = int(estudiante['edad'])
    calificaciones = estudiante['calificaciones']
    
    # Filtrar y mostrar estudiantes mayores de 18 años 
    if edad > 18:
        promedio = sum(calificaciones) / len(calificaciones)
        #cuyo promedio de calificaciones sea superior a 85.
        if promedio > 85:
            print(f"Nombre: {estudiante['nombre']}, Edad: {edad}, Promedio de Calificaciones: {promedio:.2f}")
        else:
            no_primo= True
            
            #cuya edad sea un número primo.
            for i in range(2,edad):
                x=False
               
                for j in range(i): 
                    if j==0 or j==1:
                        continue     
                    else:
                        k=i%j
                        if k==0:
                            x=True
                            break
                if x==False:
                    no_primo=False
            #cuya edad sea un número primo
            if no_primo == False:
                print(f"Nombre: {estudiante['nombre']}, Edad: {edad}, Promedio de Calificaciones: {promedio:.2f}")
        
    else:
        print(f"Nombre: {estudiante['nombre']} eres menor de 18")