var opcion = prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas");

//FUNCIONES

function boletasPagos(){
    var opBoletas = prompt("Seleccione una opción\n1.-Ver Boleta\n2.-Pagar Cuenta");
    if (opBoletas == "1") {
        alert("Haga clic aquí para descargar su boleta");
    }
    else if (opBoletas == "2"){
        alert("Usted está siendo transferido. Espere por favor...");
    }else{
        alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios");
    }
}

function senalLlamadas(){
    var opBSenal = prompt("Seleccione una opción\n1.-Problemas de Señal\n2.-Problemas con las llamadas");
    if (opBSenal == "1" || opBSenal == "2") {
        prompt("A continuación escriba su solicitud")
        alert("Estimado usuario, su solicitud: 'Tengo problemas con la señal en avenida siempre viva' Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");

    }else{
        alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios");
    }
}

function ofertaComercial(){
    var opOferta = prompt("¡Mentel tiene una oferta comercial acorde a tus necesidades \nPara conocer más información y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamará. De lo contrario ingrese 'NO'");
    if (opOferta == "SI"){
        alert("Un ejecutivo se contactará con usted");
    }else if (opOferta == "NO"){
        alert("Gracias por preferir nuestros servicios");
    }else{
        alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios");
    }
}

function otrasConsultas(){
    prompt("A continuación escriba su consulta");
    alert("Estimado usuario, su consulta: 'Quisiera saber por qué no ha llegado mi producto código 1234' Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");
    
}


opcion = parseInt(opcion);

// Evaluar la opción seleccionada
switch (opcion) {
    case 1:
        boletasPagos();
        break;
    case 2:
        senalLlamadas();
        break;
    case 3:
        ofertaComercial();
        break;
    case 4:
        otrasConsultas();
        break;
    default:
        alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios");
        break;
}
