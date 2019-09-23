
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


input.oninput= () => {
    var valor = input.value.trim(); //trim elimina los espacios al principio y final del str
    valor = document.getElementById('input').value;
    check(valor);
}

var emailOk = false;

pass.oninput= () => {
    verEstado(emailOk);
}

function check(str){

    var arroba=0;
    var punto=0;
    var charPreArroba = false;
    var charPrePunto = false;
    var charPostPunto = false;
    
    if (str==null){
        mensaje.innerHTML = 'Igrese mail por favor.';
    }

    for (l=0; l<str.length; l++){
        var $char=str.charAt(l);

        if ($char=='@')
            arroba++;
        else if ($char=='.')
            punto++;
    }

    if (str.indexOf('@') > 0)
        charPreArroba=true; // @ no puede estar en la posicion 0

    if (str.lastIndexOf('.') - str.indexOf('@') > 1)
        charPrePunto=true; // el punto precede al @ y ademas tiene q haber 1 o + char en medio

    if (str.length > str.lastIndexOf('.') + 1)
        charPostPunto=true; // . no puede estar en la ultima posicion
        
    if(arroba==1 && punto>0 && charPreArroba && charPrePunto && charPostPunto){
        mensaje.innerHTML = 'OK';
        emailOk=true;
    }else if (str.length==0)
        mensaje.innerHTML = 'Escriba su mail';
    else 
        mensaje.innerHTML = 'Mail incorrecto';
}

function verEstado(emailOk){
    if((emailOk) && (document.getElementById("pass").value != '')) {
        $('#boton_enviar').attr('disabled', false);
    } else {
        $('#boton_enviar').attr('disabled', true);
    }   
}

function ver(){
    var check = document.getElementById('checkbox1').checked;

    if(check){
        document.getElementById('pass').type = "text";
    } else {
        document.getElementById('pass').type = "password";
    }
}
function probar(){
    alert("funciona");
}

var alumnos = new Array(
    'Sebastian Bogado',
    'Juan Acevedo',
    'Daniel Sánchez',
    'Ivan Angel Medina',
    'Edgardo Sebastian Balmaceda',
    'Gutierrez Diego',
    'Emliano Mazzurque',
    'Nicolas Mamone',
    'Renato Alor',
    'Diego Benitez',
    'Matias Gomez',
    'Celia Huamani',
    'Ever Ruiz Diaz',
    'Daniel Delfino',
    'Ezequiel Pereira',
    'Ezequiel Voly Blumenfeld',
    'Mayerlin Alexandra Velasquez',
    'Rivas dueñas Mirella',
    'Vicente Gaston muñoz',
    'Gabriela Ramos')

    function verAlumno(){
        var encontro = false;
        var datoDelAlumno = document.getElementById("input").value;
        for (i = 0; i < alumnos.length; i++) {
            if(alumnos[i] == datoDelAlumno){                
                encontro = true;
                document.getElementById("nombre").innerHTML = alumnos[i];
            }
        }
        
    }