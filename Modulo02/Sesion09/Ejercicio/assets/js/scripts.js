function mostrarTexto() {
    const text2 = document.getElementById("text2");
    text2.style.display = "block"; // Muestra el div text2
}

// Función para ocultar el segundo div 
function ocultarTexto() {
    const text2 = document.getElementById("text2");
    text2.style.display = "none"; 
}

// Función para agrandar la imagen 
function agrandarImagen() {
    const img = document.getElementById("img"); 
    img.style.width="100%";
}

// Función para volver la imagen a su tamaño original
function restaurarImagen() {
    const img = document.getElementById("img"); 
    img.style.width="20%";
}

// Función para agrandar el tamaño de la letra 
function agrandarTexto() {
    const caja3Text = document.querySelector("#caja3 p");
    caja3Text.style.fontSize = "2em"; 
}