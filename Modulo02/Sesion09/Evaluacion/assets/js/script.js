var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
]

//Mostrar y ocultar el formulario de la nueva tarea
function toggleButton(){
    const formulario = document.getElementById('formulario');
    if (formulario.style.display === 'none' || formulario.style.display === '') {
        formulario.style.display = 'block';
    } else {
        formulario.style.display = 'none';
    }
}


  // Evento de clic en el botón "Agregar" dentro del formulario
  function agregarTareaBtn(){
    
    const formulario = document.getElementById('formulario');
    const nuevaTarea = document.getElementById('nuevaTarea');
    
    // Obtener el valor de la nueva tarea
    const tareaTexto = nuevaTarea.value.trim();
    if (tareaTexto === '') {
      alert('Por favor, ingrese una tarea.');
      return;
    }

    agregarTarea(tareaTexto);

    // Limpiar el campo de entrada y ocultar el formulario
    nuevaTarea.value = '';
    formulario.style.display = 'none'
  }

  function agregarTarea(tareaTexto){
    // Agrega la nueva tarea a la lista
    tareas.push({ tarea: tareaTexto });

    const cuerpoTabla = document.getElementById('cuerpo-tabla');
    // Crear una nueva fila en la tabla
    const nuevaFila = document.createElement('tr');
        
    // Crear celdas para la nueva fila
    const celdaTarea = document.createElement('td');
    const celdaFinalizar = document.createElement('td');

    // Crear un texto y un botón de finalizar
    celdaTarea.textContent = tareaTexto;
    const btnFinalizar = document.createElement('button');
    btnFinalizar.textContent = 'Finalizar';
    btnFinalizar.classList.add('btn', 'btn-danger');

    // Evento de clic en el botón "Finalizar" para eliminar la tarea
    btnFinalizar.addEventListener('click', function() {
      const index = tareas.findIndex(t => t.tarea === tareaTexto); // Encontrar el índice de la tarea
      if (index !== -1) {
          eliminarTarea(index); // Eliminar la tarea de la lista
          nuevaFila.remove(); // Eliminar la fila de la tabla
      }
    });

    // Añadir el botón de finalizar a la celda
    celdaFinalizar.appendChild(btnFinalizar);

    // Añadir las celdas a la fila
    nuevaFila.appendChild(celdaTarea);
    nuevaFila.appendChild(celdaFinalizar);

    // Añadir la fila al cuerpo de la tabla
    cuerpoTabla.appendChild(nuevaFila);
  }

 // Función para eliminar una tarea por su índice
function eliminarTarea(index) {
  tareas.splice(index, 1);
}

// Función para cargar las tareas iniciales al cargar el DOM
function cargarTareasIniciales() {
  tareas.forEach(function(item) {
      agregarTarea(item.tarea);
  });
}

// Evento para cargar las tareas iniciales cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', cargarTareasIniciales);


