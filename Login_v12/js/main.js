
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
    var arr=0;
    var punto = 0;

    if(mail.indexOf('@') !=-1) {
        arr++;
    }
    if(mail.indexOf('.') !=-1) {
        punto++;
    }
    if (arr==0 && punto == 0 ) {
        mensaje.innerHTML = "todavia te falta";
    }
    else if ((arr == 1 && punto == 0 ) || (arr == 0 && punto == 1)){
        mensaje.innerHTML = "casi .... ";
    }
    else if (arr == 1 && punto == 1) {
        mensaje.innerHTML = "Perfecto";
    }
}