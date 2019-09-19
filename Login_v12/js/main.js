
(function ($) {
    "use strict";

    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);

// -----------------------------------------------------------------

// NUESTRO CODIGO VA ACÁ
// CHEQUEA QUE HAYAMOS INGRESADO UNA CUENTA DE EMAIL Y MUESTRA LA CONSTRASEÑA

// function ver()
// {
//     if
//     (document.getElementById('checkbox1').checked = 1)
//     {
//         document.getElementById('pass').type = "text";
//     } 
//     else if 
//     (document.getElementById('checkbox1').checked = 1) 
//     {
//         document.getElementById('pass').type = "password";
//     }
// }

function ver()
{
        if (document.getElementById('pass').type == "text")
        document.getElementById('pass').type = "password";
        else if (document.getElementById('pass').type == "password") 
        document.getElementById('pass').type = "text";
}


input.oninput = function () {
    var valor = input.value;
    check(valor);
}

function check(mail){
    var arrobaIngresado=0;
    var punto = 0;
    // var arrobas = 1;
    // var arrobasCantidad = mail.match(/@/g).length ;
    // if (mail.match(/@/g).length = null) {
    arrobasCantidad = 0;
    // console.log(arrobasCantidad);
    

    if(mail.indexOf('@') !=-1) {
        arrobaIngresado++;
    }
    if(mail.indexOf('.') !=-1) {
        punto++;
    }
    if ((arrobaIngresado + punto + arrobasCantidad) == 1 ) {
        mensaje.innerHTML = "todavia te falta";
    }
    else if ((arrobaIngresado + punto + arrobasCantidad) > 1 && (arrobaIngresado + punto + arrobasCantidad) < 3  && (arrobaIngresado + punto + arrobasCantidad) > 3 ){
        mensaje.innerHTML = "casi .... ";
    }
    else if ((arrobaIngresado + punto + arrobasCantidad) == 2 ) {
        mensaje.innerHTML = "Perfecto";
    }
    
    console.log(arrobasCantidad);
}

// MEJORAR LA FUNCION CHECK PARA QUE DETECTE UN CARACTER ANTES QUE EL '@' UNO POSTERIOR Y UN PUNTO POSTERIOR

// DESACTIVAR EL BOTON HASTA QUE SE HAYAN COMPLETADOS LOS 2 CAMPOS CORRECTAMENTE

// VALIDAR EL LOGIN CUANDO LE DEMOS AL BOTON, MOSTARLO COMO ALERT, (VALIDAR CONTRA UN ARRAY)