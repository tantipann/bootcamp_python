var bandera = false;
var opcion = "";
var saldo = 0;

function Cliente(nombre, identificador, clave, saldo) {
      this.nombre = nombre;
      this.identificador = identificador;
      this.clave = clave;
      this.saldo = saldo;


  }
  
 
  var cliente1 = new Cliente("Juan Pérez", "JP001", "contraseña123", 1000);
  var cliente2 = new Cliente("Patricia Torres", "PT01","pt123",1500);
  var cliente3 = new Cliente("Pepita Leal","pl002", "1234",5000);

  id=prompt("Ingrese su identificador");
  clave = prompt("Ingrese su clave");
  if (id==cliente1.identificador && clave == cliente1.clave){
    saldo = cliente1.saldo
    bandera = true;
    
  }else if(id==cliente2.identificador && clave == cliente2.clave){
    saldo = cliente2.saldo
    bandera = true;
  }else if(id==cliente3.identificador && clave == cliente3.clave){
    saldo = cliente3.saldo
    bandera = true;
  }else{
    alert("Usuario o clave incorrectas");
  }

while (bandera == true){
    opcion = prompt("Seleccione que desea hacer: \n1.- Ver saldo \n2.- Relizar giro \n3.- Realizar deposito  \n4.- Salir");
    if (opcion == "1"){
        alert("Su saldo es " + saldo);
    }else if (opcion == "2"){
        girar = prompt("Su saldo actual es: " + saldo + "\nIngrese el monto que desea girar");
        girar = parseInt(girar);
        if (girar > saldo){
            alert("No puede girar una cantidad mayor a su saldo");
        }else{
            saldo = saldo - girar;
            alert("Giro realizado. Su nuevo saldo es " + saldo)
        }
    }else if (opcion == "3"){
        deposito = prompt("Su saldo actual es: " + saldo + "\nIngrese el monto que desea depositar");
        deposito = parseInt(deposito);
        saldo = saldo + deposito;
        alert("Deposito realizado. Su nuevo saldo es " + saldo)
    
    }else if (opcion == "4"){
        alert("Saliendo del programa, Gracias por preferirnos");
        bandera = false
    }
}
