$(document).ready(function () {
    $("#regis").submit(function (e) {
        
        
        /*Variables */
        var nombreu = $("#nombre").val();
        var direc = $("#direccionu").val();
        var rut = $("#rutusu").val();
        var tel = $("#celu").val();
        var correo = $("#gmail").val();
        var pass = $("#contra").val();
        var pass2 = $("#conficlave").val();
        var resp = $("#resp").val();


        /*Mensajes */
        let msj1 = "";
        let msj2 = "";
        let msj3 = "";
        let msj4 = "";
        let msj5 = "";
        let msj6 = "";
        let msj7 = "";
        let msj8 = "";
        let msj9 = "";

        /*Bandera */
        let enviar = false;
        let compro = false;

        /*Regex de validacion */
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
        let regexname = /[0-9]/
        let regexpassword = /(?=^.{6,12}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/

        /*Validaciones del Nombre */
        if (nombreu.trim().length < 3 || nombreu.trim().length > 10) {
            msj1 += "El nombre debe contener entre 3 y 10 caracteres<br>";
            enviar = true;
        }
        if (regexname.test(nombreu)) {
            msj1 += "El nombre no debe contener numeros<br>";
            enviar = true;
        }

        var letra = nombreu.charAt(0);
        if (!esMayuscula(letra)) {
            msj1 += "La primera letra debe ser mayúscula<br>";
            enviar = true;
        }

        if (enviar) {
            $("#aviso1").html(msj1);
        }else{
            $("#aviso1").html("");
        }


        /*Validaciones de Apellido */
        if (direc.trim().length < 1 || direc.trim().length > 60) {
            msj2 += "La dirección debe contener entre 1 y 60 caracteres<br>";
            enviar = true;
        }

        if (enviar) {
            $("#aviso2").html(msj2);
        }else{
            $("#aviso2").html("");
        }

        /*Validaciones de Rut */
        if (rut.trim().length < 8 || rut.trim().length > 9) {
            msj3 += "Ingrese un rut valido<br>";
            enviar = true;
        }
        if (enviar) {
            $("#aviso3").html(msj3);
        }else{
            $("#aviso3").html("");
        }


        /*Validaciones de Telefono */
        if (tel.trim().length < 9 || tel.trim().length > 9) {
            msj4 += "Ingrese un teléfono valido<br>";
            enviar = true;
        }
        if (enviar) {
            $("#aviso4").html(msj4);
        }else{
            $("#aviso4").html("");
        }
        /*Validaciones de Correo */
        if (!regexEmail.test(correo)) {
            msj5 += "El correo no es válido<br>";
            enviar = true;
        }
        if (enviar) {
            $("#aviso5").html(msj5);
        }else{
            $("#aviso5").html("");
        }


        /*Validaciones de Contraseña */
        if (!regexpassword.test(pass)) {
            msj6 += "La contraseña debe contener Un largo Min de 6 y un Max de 12 Caracteres<br>1 Número<br> 1 Minúscula <br>1 Mayúscula<br> 1 Carácter Especial";
            enviar = true;
        }

        if (enviar) {
             $("#aviso6").html(msj6);
        }else{
            $("#aviso6").html("");
        }

        /*Validaciones de Contraseña 2 */
        if (!regexpassword.test(pass2)) {
            msj7 += "La contraseña debe contener Un largo Min de 6 y un Max de 12 Caracteres<br>1 Número<br> 1 Minúscula <br>1 Mayúscula<br> 1 Carácter Especial";
            enviar = true;
        }

        if (enviar) {
             $("#aviso7").html(msj7);
        }else{
            $("#aviso7").html("");
        }

        /* Validaciones contraseñas iguales */
        console.log(pass)
        console.log(pass2)
        if(pass != pass2){
            
            msj9 += "Las Contraseñas no son iguales";
            enviar = true;
        }

        if(enviar){
            $("#aviso9").html(msj9);
        }else{
            $("#aviso9").html("");

        }

        /*Validaciones de Respuesta de Seguridad */
        if(!regexname.test(resp)){
            msj7 += "La respuesta no debe contener números";
            enviar = true;
        }
        if (enviar) {
            $("#aviso8").html(msj8);
        }else{
            $("#aviso8").html("");
        }

        if(compro == enviar){
            $("#aviso").html("Enviado");
        }else{
            
        }

    });

    function esMayuscula(letra) {
        if (letra == letra.toUpperCase()) {
            return true;
        }
        else {
            return false;
        }
    }
});