function ejercicio_3() {
    //Desarrollar un programa que muestre la tabla de multiplicar de un n�mero ingresado po4 teclado.

        var num = parseInt(prompt('Ingrese un número para obtener su tabla: '));
        for (i = 1; i < 11; i++) {
            var producto = num * i;
            alert(num + 'x' + i + '=' + producto);
        }
    }