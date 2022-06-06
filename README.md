# SOLUCION-PARCIAL-3
Ubicación del tercer parcial de programación Uniquindio
# SOLUCION-PARCIAL-3
Ubicación del tercer parcial de programación Uniquindio

OPCIÓN 1
1. Descargar un archivo en formato CSV o TXT de la página
https://www.datos.gov.co/browse?sortBy=newest&utf8= %E2 %9C %93 y hacer una
librería con un programa externo que la importe.
a) La librería debe definir al menos dos tipos de datos (Usando en al menos uno de
ellos la herencia y el comando super).
b) Al definir un objeto de las clases definidas, una de las variables debe ser una ruta
del computador en donde tengan un archivo de datos a leer (csv o txt). El archivo
debe ser leido y almacenado correctamente en una o mas variables en donde cada
dato sea del tipo que debería ser. Es decir, una columna de edad debe ser leída
como un entero.
c) En cada clase se deben redefinir al menos cuatro métodos mágicos entre los que
debe estar el str.
d) Uno de los objetos definidos debe ser mutable y permitir itemización.
e) Uno de los métodos definidos debe exportar graficas de matplotlib a partir de las
columnas de la tabla de datos que se hubiera leído en el método __init__
f ) El programa debe ser útil en algo concerniente a la física, las matemáticas o la
ciencia de datos y debe evidenciarse en el programa externo que la importa.

1.	Se realizo la descarga del archivo https://www.datos.gov.co/Ciencia-Tecnolog-a-e-Innovaci-n/Personas-Capacitadas-en-Habilidades-Digitales/nzyx-5vfw. Un archivo de 78 filas por 10 columnas lo suficientemente amplio para poder mostrar el manejo de datos y realizar algunas gráficas estadísticas.

2.	Se creo una librería con el nombre modulo 1 la cual en su interior tiene un archivo de funciones. Las funciones creadas fueron las siguientes.

•	Formatear datos: Aplica un formato a los datos de la tabla
•	Verificación de ruta
•	Creación de leyenda para la gráfica de barras y de puntos
•	Creación de leyenda para la gráfica con porcentajes

3.	Se crearon las dos estructuras de datos solicitadas:

•	DatosG: Para tomar los datos de la tabla y utilizarlos posteriormente
•	Multigrafics: Para la creación de las graficas con los datos tomados de la tabla

4.	DatosG: Esta estructura de datos esta compuesta por cuatro métodos mágicos, (__str__), (__eq__), (__ge__), (__le__). Más el método constructor (__init__).
Dentro de esta estructura están 6 métodos definidos:
•	Mostrar data
•	Lista datos
•	Nombre columnas
•	Dimensiones
•	Cantidad de ….en….
•	Columnas sin repetir

5.	Multigrafics: Compuesta por herencia de la estructura de datos anterior, por lo cual podemos emplear todos los métodos definidos listados en el numeral 4. utilizamos “super” para inicializarla con una dirección de archivo, sin embargo, la estructura de datos anteriores itemizable, es decir que podemos ingresar a esa estructura la anterior y utilizar sus datos para sus diferentes métodos. Está compuesta por los mismos cuatro métodos mágicos de DatosG. Tenemos los siguientes métodos definidos. (Se utilizo la librería matplotlib)
•	Grafica de puntos
•	Gráfica de barras
•	Gráfica de porcentajes

6.	Programa externo: Este emplea la librería creada para solucionar un ejercicio puntual de manejo de información orientado a la ciencia de datos. Este consiste en dos métodos “main” y “menu”, el primero es la función principal en la cual se ingresa la dirección del archivo, se corrigen malos ingresos y se crea un objeto de la primera estructura de datos. La segunda publica un menú de 7 opciones para el usuario que se pueden ver en el código del programa. De la 1-3 se emplea la DatosG y de la 4-6 Multigrafics y una opción de salida. 
