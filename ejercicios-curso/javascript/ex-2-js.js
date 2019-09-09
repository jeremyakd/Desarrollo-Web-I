function ejercicio_2() {
    //Desarrollar un programa que solicite la carga de 10 n�meros e imprima la suma de lo �ltimos 5 valores ingresados.

        var suma = 0;

        for (i = 0; i < 10; i++) {
            var num = parseInt(prompt('Ingrese el ' + (i + 1) + '° numero: '));
            if (i > 4)
                suma += num;
        }
        alert('la suma de los ultimos 5 numeros es: ' + suma);
    }
