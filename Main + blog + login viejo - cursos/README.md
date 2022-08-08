# A) Primeros pasos:
-Descargar la carpeta contenedora del proyecto para abrir en vsc.
-Abrir el vsc y seleccionar open folder.
-Seleccionar la carpeta dentro de la ruta de descarga elegida.


## B) Iniciar la consola:
Dentro del vsc, nos encontraremos en la esquina superior izquierda, un menu con varias herramientas y opciones.

Presionamos click izuqierdo la opcion de "Terminal" que nos despliega un subcartel con varias opciones. Seleccionamos "New Terminal". Al hacerlo, vemos que se crea una seccion en la parte inferior de la pantalla.

Para encender el servidor local, escribimos en la terminal:
---- python manage.py runserver ----
                o
---- py manage.py runserver

Luego de unos segundos, la terminal te presentara el link de la pagina del servidor local hecha con django. Parese sobre el link y se le aparecera una ventana con un hipervinculo hacia la pagina y seleccionela.


# C) Comandos a elegir:
Una vez dentro, te indicara que la pagina no se ha encontrado, por lo que debemos ejecutar el comando de forma manual en la url del navegador en uso.
admin/
mi-pagina/
listar-cursos/
listar-estudiantes/
listar-profesores/
formulario_curso/
contacto/
busqueda_productos/
buscar_curso/
formulario_profesores/
formulario_estudiante/


# D) Pagina Principal:
Dentro de la lista de url disponibles para utilizar, nos dirigimos hacia " mi-pagina/ ". Para ello debemos colocar ese comando al lado de http://127.0.0.1:8000/ (no olvidarse de la barra).
Una vez hecho eso nos vamos a encontrar con la pagina principal y sus respectivas opciones para interacturan, junto con la estructura y parrafos dentro de la misma.


# E) Listas:
En la parte superior de la pagina principal, nos encontraremos con las diferentes opciones. De momento hasta esta etapa del proyecto, nos encontraremos con:
-Cursos
-Estudiantes
-Profesores
Al hacer Click Izquierdo en cada una de estas opciones, nos encontraremos con listas para cada clase:
-Cursos: cada uno de los cursos inscriptos con nombre de curso y camada,
-Estudiantes: aquellos inscriptos con nombre, apellido y mail.
-Profesores: con nombre, apellido, mail y profesion en la que se especializan.


# F) Formularios:
Ademas de las listas en la barra superior, tenemos 3 formularios, para cada una de las clases anteriores. Se las selecciona y cada de ellas te pedira que completes los datos en cada una de los campos de informacion. Cabe Aclarar que el sistema no va a tomar datos incorrectos en las secciones de numeros y mails, Si te pide numero y colocas letras, te va a pedir que lo cambies.
Esto ultimo tambien aplica para los mails, sin el @no lo va a tomar como valido.

Si todos los datos introducidos son correctos, se te mostrara en la pantalla que los datos que has ingresado han sido guardados. Para verificar de ello, volvemos a las listas y podes corroborar que efectivamente se ha registrado en la base de datos.


# G) Buscar:
Hasta el momento, se tendra la herramienta para buscar algun nombre dentro de los cursos registrados en la base de datos. La opcion se encuentra como " Buscar Cursos ". Al entrar en ella te pedira que completes el campo con algun nombre de un curso que creas que este. 
Si efectivamente el nombre del curso se encuentra en el sistema, la pagina te devolvera todos los cursos que esten bajo el nombre introducido y sus diferentes numeros de camada.
Si el nombre no se encuentra, te indicara que no existen cursos con ese nombre.



# H)Fin:
Una vez que haya terminado de probar las diferentes funciones de la pagina, vuelva al vsc, haga click en la terminal y presione las teclas "Ctrl" + "C" para cerrar el servidor.
-Tambien se puede cerrar el servidor con cerrar el programa, que forzara el cierre de la aplicacion y la conexion con el servidor local.
