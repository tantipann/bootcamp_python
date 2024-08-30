var numero1, numero2;

numero1 = prompt("Ingrese el primer numero");
numero2 = prompt("Ingrese el segundo numero")

numero1 = parseInt(numero1)
numero2 = parseInt(numero2)

if (numero1 > numero2){
    alert(numero1 + " es mayor que " + numero2);
} else if (numero2 > numero1) {
    alert(numero2 + " es mayor que " + numero1);
} else {
    alert("Ambos números son iguales.");
}