$(document).ready(function () {
  // Ocultar todos los detalles al inicio
  $(".detalles").hide();

  let detalleVisible = null;

  // Función para mostrar el detalle correspondiente
  function mostrarDetalle(detalleId) {
    // Si hay un detalle visible y es diferente del que se quiere mostrar
    if (detalleVisible && detalleVisible !== detalleId) {
      $(detalleVisible).hide();
    }
    // Mostrar el nuevo detalle con toggle para alternar la visibilidad
    $(detalleId).toggle();
    detalleVisible = $(detalleId).is(":visible") ? detalleId : null;
  }

  // Manejar el clic en los botnes "Ver más" 
  $("#Baires").click(function () {
    mostrarDetalle("#detallesBaires");
  });

  $("#MachuPicchu").click(function () {
    mostrarDetalle("#detallesMachuPicchu");
  });

  $("#Rio").click(function () {
    mostrarDetalle("#detallesRio");
  });

  // Manejar el clic en el botón de cerrar (X) de los detalles
  $(".btn-close").click(function () {
    $(this).closest(".detalles").hide();
    detalleVisible = null;
  });
});
