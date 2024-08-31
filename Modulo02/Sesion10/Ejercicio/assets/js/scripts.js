$(document).ready(function () {
  //Para mostrar el segundo div
  $("#text1").mouseover(function () {
    $("#text2").show();
  });

  //Para ocultar el segundo div
  $("#text1").mouseleave(function () {
    $("#text2").hide();
  });

  //Para agrandar la imagen
  $("#caja2").click(function () {
    $("#img").css("width", "100%");
  });

  // Para volver la imagen a su tamaño original
  $("#caja2").mouseleave(function () {
    $("#img").css("width", "20%");
  });

  // para agrandar el tamaño del texto
  $("#caja3").dblclick(function () {
    $("#caja3 p").css("font-size", "2em");
  });
});
