function ejercicio_5() {
    //Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 -16 -24, etc.
    var multiplos = 8;
    var str = '';
    while (multiplos < 500) {
        str += (multiplos + ' - ');
        multiplos += 8;
    }
    str=recortarUltimosChar(str);
    alert(str);
}

function recortarUltimosChar(str){
    //Este método recorta los últimos char para que no finalice la serie con '-'
    return str.substr(0,str.length-2);
}