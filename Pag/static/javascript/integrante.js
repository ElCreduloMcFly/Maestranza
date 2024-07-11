function actualizarSelects() {
    // Obtener los valores seleccionados
    var integrante1 = document.getElementById('integrante1').value;
    
    // Desactivar las opciones seleccionadas en integrante2
    var integrante2 = document.getElementById('integrante2');
    for (var i = 0; i < integrante2.options.length; i++) {
        if (integrante2.options[i].value === integrante1) {
            integrante2.options[i].disabled = true;
        } else {
            integrante2.options[i].disabled = false;
        }
    }
    
    // Desactivar las opciones seleccionadas en integrante3
    var integrante3 = document.getElementById('integrante3');
    for (var j = 0; j < integrante3.options.length; j++) {
        if (integrante3.options[j].value === integrante1) {
            integrante3.options[j].disabled = true;
        } else {
            integrante3.options[j].disabled = false;
        }
    }
}

// Llamar a la función al cargar la página
window.onload = function() {
    actualizarSelects();
};