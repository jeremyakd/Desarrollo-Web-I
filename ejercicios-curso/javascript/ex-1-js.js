function medio(){
    var it = document.getElementById("numero").value;
    ejericio_1(it);
}


function ejericio_1(iterador) {
    /*
        Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:

        a)	La cantidad de valores negativos ingresados.
        b)	La cantidad de valores positivos ingresados.
        c)	La cantidad de múltiplos de 15.
        d)	El valor acumulado de los números ingresados que son pares.
    */
        
        var countPositivos=0;
        var countNegativos=0;
        var countMultiplos15=0;
        var sumaPares=0;       

        for (i = 0; i < iterador; i++) {
            var ingreso = parseInt(prompt('Ingrese el ' + (i + 1) + '° número: '));

            if (ingreso > 0)
                countPositivos++;
            else if (ingreso < 0)
                countNegativos++;

            if (ingreso > 15 && ingreso % 15 == 0)
                countMultiplos15 += 1;
            else if (ingreso != 0 && ingreso % 2 == 0)
                sumaPares += ingreso;
        }

        str='Cantidad de numeros negativos: ' + countNegativos + '\n' + 
            'Cantidad de numeros positivos: ' + countPositivos + '\n' +
            'Cantidad de numeros multiplos de 15: ' + countMultiplos15 + '\n' + 
            'Suma de numeros pares: ' + sumaPares;
        
        alert(str);
    }
