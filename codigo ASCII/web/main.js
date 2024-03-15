document.addEventListener("keydown", function(event) {
    var asciiDisplay = document.getElementById("ascii-display");
    var key = event.key;
    var keyCode = event.keyCode;
    var asciiCode;
  
    // Manejo especial para teclas especiales
    if (key === " " || key === "Enter" || key === "Delete") {
      asciiCode = keyCode;
    } else {
      asciiCode = key.charCodeAt(0);
    }
  
    asciiDisplay.textContent = "La tecla '" + key + "' fue presionada. Código ASCII: " + asciiCode;
  });
  
    