#   1- Dados dos números enteros cualquiera almacenados en variables, almacenar en
#  una nueva variable la suma de ellos e imprimir por pantalla su resultado.

#  numero1 = 1;
#  numero2 = 2;
#  suma = numero1 + numero2;

#  print(suma);

#-----------------------------------------------------#

#  2- Dados dos números enteros cualquiera almacenados en variables, almacenar en
# una nueva variable la resta de ellos e imprimir por pantalla su resultado.

#  numero1 = 1;
#  numero2 = 2;
#  resta = numero1 - numero2;

# print(resta);

#-----------------------------------------------------#

# 3- Solicitar al usuario el ingreso de dos números enteros. Calcular (utilizando
# distintas variables), su suma, resta, multiplicación y división. Mostrar por
# pantalla el resultado de cada una de las operaciones realizadas. Por ej. si el
# usuario ingresó 4 y 7. Mostrar “El resultado de multiplicar 4 x 7 es 28”.


# print("Por favor ingresar dos numeros enteros");
# numero1 = int(input());
# numero2 = int(input());
# print(f"El resultado de sumar numero1 y numero2 es {numero1+numero2}");
# print(f"El resultado de restar numero1 y numero2 es {numero1-numero2}");
# print(f"El resultado de dividir numero1 y numero2 es {numero1/numero2}");
# print(f"El resultado de multiplicar numero1 y numero2 es {numero1*numero2}");

#-----------------------------------------------------#

# 4- Solicitar al usuario el ingreso de su nombre, luego de su apellido (dos ingresos).
# Luego mostrar por pantalla un mensaje de bienvenida completo. Por ej., si
# ingresó Julián Alvarez: “¡¡Bienvenido Julián Alvarez!!” (utilizando una variable
# para nombre y otra para apellido).

# print("Ingresa tu Nombre:");
# name = str(input());
# print("Ingresa tu Apellido:");
# lastName = str(input());

# print(f"Bienvenido {name} {lastName}!!");

#-----------------------------------------------------#

# 5- Ídem ejercicio 4 pero una vez ingresados nombres y apellidos, almacenarlos en
# una sola variable y mostrar el mensaje de bienvenida.

# print("Ingresa tu Nombre:");
# name = str(input());
# print("Ingresa tu Apellido:");
# lastName = str(input());

# fullName = (f"{name} {lastName}");
# print(f"Bienvenido {fullName}!!");

#-----------------------------------------------------#

# 6- Solicitar al usuario el ingreso de dos números, calcular y mostrar el promedio de
# ambos valores.

# print("Ingrese dos numeros para calcular su promedio");
# numero1 = int(input());
# numero2 = int(input());

# promedio = (numero1+ numero2)/2;

# print(f"El promedio es {promedio}");

#-----------------------------------------------------#

# 7- Solicitar al usuario el ingreso de una palabra cualquiera, y mostrarle por pantalla
# cuántas letras tiene la palabra ingresada.

# palabra = str(input());
# print(len(palabra));


#-----------------------------------------------------#

# 8- Solicitar al usuario el ingreso de la BASE y la ALTURA de un triángulo, calcular y
# mostrar el área del triángulo.

# print("Ingrese la BASE del triangulo en cm");
# base = int(input());
# print("Ingrese la ALTURA del triangulo en cm");
# altura = int(input());

# area = (base * altura) / 2

# print(f"El area del triangulo es {area}cm2");

#-----------------------------------------------------#

# 9- Solicitar al usuario el ingreso de 3 palabras y armar un acrónimo con ellas. De
# cada palabra debe tomar la primera letra y armar el acrónimo. Ejemplo: Qatar,
# Argentina y Mundial --> QAM. Mostrar el resultado por pantalla.

# print("Ingrese 3 palabras por separado");

# palabra1 = str(input());
# palabra2 = str(input());
# palabra3 = str(input());

# acronimo = palabra1[0] + palabra2[0] + palabra3[0];

# print(f"{acronimo}");

#-----------------------------------------------------#

# 10- Solicitar al usuario el ingreso del total de alumnos del curso, luego la cantidad de
# mujeres y la cantidad de varones. Calcular y mostrar el porcentaje de varones y
# mujeres de la clase.

# print("Ingrese el total de alumnos del curso");
# totalAlumnos = int(input());
# print("Ingrese el total de varones del curso");
# totalVarones = int(input());
# print("Ingrese el total de mujeres del curso");
# totalMujeres = int(input());

# porcentajeVarones = (totalVarones * 100) / totalAlumnos;
# porcentajeMujeres = (totalMujeres * 100) / totalAlumnos;

# print(f"el porcentaje de varones es {porcentajeVarones}% y el de mujeres {porcentajeMujeres}%");

#-----------------------------------------------------#

# 11- Solicitar al usuario el ingreso de dos palabras y armar combinaciones con ellas.
# De la primera palabra tome las primeras tres letras, utilice el operador “:”. De lasegunda palabra tome las primeras dos letras, utilice el operador “:”. Formar una
# nueva palabra con los recortes solicitados y mostrarlo por pantalla.

# print("Ingrese dos palabras: ");
# palabra1 = str(input());
# palabra2 = str(input());

# palabraFinal = palabra1[:3] + palabra2[:2];

# print(palabraFinal);

#-----------------------------------------------------#

# 12- Realice una calculadora, el usuario ingresará dos números reales y se deberán
# calcular todas las operaciones entre ellos: A) Suma; B) Resta; C) Multiplicación;
# D) División; E) Exponente/Potencia. Para todos los casos se debe imprimir en
# pantalla el resultado aclarando la operación realizada en cada caso y con que
#  números se ha realizado la operación. Por ej: “La suma entre 14.1 y 6.4 es 20.5”

# print("Ingrese dos numeros: ")
# numero1 = int(input());
# numero2 = int(input());

# print(f"La suma entre {numero1} y {numero2} es {numero1+numero2}");
# print(f"La resta entre {numero1} y {numero2} es {numero1-numero2}");
# print(f"La division entre {numero1} y {numero2} es {numero1/numero2}");
# print(f"La multiplicacion entre {numero1} y {numero2} es {numero1*numero2}");
# print(f"La potencia entre {numero1} y {numero2} es {numero1**numero2}");

#-----------------------------------------------------#

# 13- Realice un programa que solicite al usuario el nombre completo de la persona,
# el DNI de la persona, la edad de la persona y la altura de la persona. Luego el
# programa debe mostrar por pantalla dos líneas de texto por separado:
# a. En una línea imprimir el nombre completo y el DNI, aclarando de que
# campo se trata cada uno. Por ej.: Nombre Completo: Elena Lobo, DNI:
# 38041532.
# b. En la segunda línea se debe imprimir el nombre completo, edad y altura
# de la persona. Nuevamente debe aclarar el campo de cada uno, para el
# que lo lea entienda de que se está hablando.


# 14- Realice un programa que solicite al usuario el ingreso de un nombre completo.
# Luego lo muestre por pantalla en los siguientes formatos:
# a. Todas las letras en minúsculas
# b. Todas las letras en mayúsculas
# c. Solo la primera letra del nombre en mayúscula

print("Ingrese su nombre completo:")
nombre = str(input());

print(nombre.upper());
print(nombre.lower());
print(nombre.capitalize());








