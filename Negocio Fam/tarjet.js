console.log("El archivo JavaScript se está ejecutando correctamente.");


const btnHome = document.getElementById("home");
const btnMenu = document.getElementById("menu");
const tarjHome = document.getElementById("tarjetaHome");
const tarjMenu = document.getElementById("tarjetaMenu");

btnHome.addEventListener('click', function() {
    tarjHome.classList.remove("hidden");
    tarjMenu.classList.add("hidden");
});

btnMenu.addEventListener('click', function() {
    tarjHome.classList.add("hidden");
    tarjMenu.classList.remove("hidden");
});


// Obtener todos los elementos <li> con la clase 'numbers'
const numbersList = document.querySelectorAll('.numbers li');

// Iterar sobre cada elemento <li>
numbersList.forEach(function(numberElement) {
    // Obtener el número de teléfono
    const phoneNumber = numberElement.textContent.trim();

    // Redireccionar al hacer clic en el número
    numberElement.addEventListener('click', function() {
        window.location.href = `tel:${phoneNumber}`;
    });

    // Copiar al portapapeles al hacer doble clic en el número
    numberElement.addEventListener('dblclick', function() {
        // Crear un elemento de texto temporal
        const tempInput = document.createElement('textarea');
        tempInput.value = phoneNumber;
        document.body.appendChild(tempInput);
        // Seleccionar y copiar el contenido del elemento de texto temporal
        tempInput.select();
        document.execCommand('copy');
        // Eliminar el elemento de texto temporal
        document.body.removeChild(tempInput);
        // Alerta al usuario que el número ha sido copiado
        alert(`Número ${phoneNumber} copiado al portapapeles`);
    });
});

