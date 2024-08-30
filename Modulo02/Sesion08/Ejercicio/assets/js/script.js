var bandera = true;
var opcion = "";


while (bandera == true){
    opcion = prompt("Menu \nEscribe el número de la opción que buscas: \n1.- Ingreso de Estudiante \n2.- Modificación de estudiante \n3.- Eliminación de estudiante  \n4.- Agregar Notas\n5.- Salir");
    if (opcion == "5"){
        alert("Saliendo del programa, Gracias por preferirnos");
        bandera = false
    }
}
