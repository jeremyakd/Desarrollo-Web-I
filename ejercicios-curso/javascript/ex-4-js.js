function ejercicio_4() {
    //Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado).

    var aux = 1;
    var str = '';
    while (aux < 26) {
        str += (11 * aux) + ' - ';
        aux += 1;
    }
    str = recortarUltimosChar(str);
    alert(str);
}

function recortarUltimosChar(str){
    //Este método recorta los últimos char para que no finalice la serie con '-'
    return str.substr(0,str.length-2);
}



