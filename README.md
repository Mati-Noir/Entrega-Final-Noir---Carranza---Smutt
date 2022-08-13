# IMPORTANTE  (LEER ANTES DE USAR)

# Para poder probar y testear correctamente el proyecto final, se debe descargar el archivo zip de la branch_funcional.

# Si se descarga o se pushea otra branch o la main, el proyecto que incorporara su maquina no sera el producto final a mostrar

# Con esa carpeta descargada del archivo.zip, extraerla y utilizarla dentro del Visual Studio Code.

# Hay una version actualizada dentro de la branch_funcional_Correccion. (Incluye Edit Profile + Cambio de Contraseña)

# A) Primeros pasos:
-Descargar la carpeta contenedora del proyecto para abrir en vsc.

-Abrir el Visual Studio Code y seleccionar "open folder".

-Seleccionar la carpeta dentro de la ruta de descarga elegida.

# B) Iniciar la consola, detalles y requisitos:
Dentro del vsc, nos encontraremos en la esquina superior izquierda, un menu con varias herramientas y opciones.

Presionamos click izuqierdo la opcion de "Terminal" que nos despliega un subcartel con varias opciones. Seleccionamos "New Terminal". Al hacerlo, vemos que se crea una seccion en la parte inferior de la pantalla.

Antes de encender el servidor u realizar cualquier comandod de la terminal, debemos verificar que estemos en la carpeta correcta. En este caso, el ultimo archivo de la carpeta debe estar bajo el nombre:

Entrega-Final-Noir---Carranza---Smutt

Si escribimos algun comando en la terminal sin estar en la carpeta correcta, nos saldra al final este error:

....... can't open file .... [Errno 2] No such file or directory

Para evitar que nos pase esto, debemos ingresar lo siguiente:

cd Entrega-Final-Noir---Carranza---Smutt

Una vez hecho esto, nos debemos asegurar que tengamos las aplicaciones necesarias para que el proyecto funcione.

Dentro del archivo requirements.txt, estaran las versiones de los programas fundamentales para que el proyecto funcione. Si usted no los tiene, entonces realize lo siguiente:

pip install -r requirements.txt

La instalacion se realizara por si sola, por lo que espere hasta que haya finalizado para proseguir.

# C) Ejecutar el servidor local:
Hasta ahora, estamos en la ubicacion correcta de la carpeta, instalamos los programas requeridos para que el proyecto a revisar funcione, pero necesitamos prender el servidor local de django.

Como se hace? Nos vamos a la terminal y escribimos:

python manage.py runserver

o tambien puede ingresar:

py manage.py runserver

Luego de unos segundos, la terminal te presentara el link de la pagina del servidor local hecha con django "http://127.0.0.1:8000/". Parese sobre el link y se le aparecera una ventana con un hipervinculo hacia la pagina y seleccionela.

# D) Navbar
Una vez dentro, te dirigira hacia la pagina principal, donde nos encontraremos con las diferentes opciones del menu superior, el contenido de presentacion del proyecto, su tematica hasta el final con las ultimas opciones del pie de pagina.

Los botones interactivos de la barra superior se componen de:

-Home/Inicio: Su funcion es regresar al menu principal, estando en las diferentes secciones del proyecto, para no regresar de forma manual por medio del navegador.

-Reseñas: Aca presentamos un modelo de CRUD en el cual invitamos a los usuarios con la posibilidad de poder expresar sus criticas o ovaciones a los juegos que deseen a su gusto. El autor podra elegir el titulo, contexto y una foto para dar su opinion.Los articulos se encontraran en un catalogo expositorio para todo aquel que desee leerlo.

-Agregar Reseñas: En esta seccion, tal cual como su nombre lo indica, puede crear articulos para poder publicarlos en la listview del panel de reseñas.

-Iniciar Sesion: Como toda pagina, tenemos una seccion para crear usuario y poder logearse. Ser un usuario dentro del proyecto, tendra acceso a la composicion de reseñas. Al momento de ingresar los datos, se te solicitara que completes los campos con la informacion correcta. Si usted no tiene usuario, puede completar el formulario dentro de la opcion de registrarse y intentar nuevamente.

-Registrarse: Estando sin iniciar sesion, se presentaran 2 opciones dentro del navbar, siendo el iniciar sesion y registrarse ambos botones. Al hacer click, le enviara hacia un formulario a completar con sus datos. Una vez completo, confirme y le redirigira hacia la pestaña de login, inicie sesion y pronto estara en el menu principal junto con una frase de bienvenida y el nombre de usuario elegido.

Las nuevas opciones que se encontraran disponibles en la branch_funcional_Correccion son:

-Modificar Perfil:
En esta seccion podras modificar tus datos y agregar en caso de que falten. Tambien se presentara la posibilidad de actualizar la contraseña, requeriendo ingresar la contraseña vieja para poder crear la nueva contraseña. Al hacerlo, se le indicara que la operacion ha sido exitosa.

# E) Contenido de Presentacion:
Ademas de la barra de navegacion superior, se encontrara con informacion de presentacion y bienvenida al usuario. Normalmente se explica de que se trata el proyecto y que funciones apuntamos a desempeñar.

# F)Footer/Pie de Pagina:
Al desecender hasta el final, se encontrara con el pie de pagina y sus respectivos links adicionales. Estos hipervinculos te llevaran hacia:

-About us: Con informacion sobre los autores del proyecto, la institucion, el tutor y profesor a cargo dentro del periodo de cursada y correcciones.Estara la opcion para poder visitar el perfil de los profesor en GitHub, junto con el tutor y el sitio web de la plataforma.Tambien se encuentran los links a los github de los integrantes en caso de buscar mas información.

-Términos y Condiciones: Textos explicativos sobre que usted puede hacer y que no dentro del proyecto.

-Politicas de Privacidad: Similiar al punto anterior pero con detalles de como se utiliza sus datos introducidos en la base de datos del proyecto y nuestra postura al respecto.

Tambien estaran las opciones de redes sociales, todas redirigidas hacia las páginas oficiales de la institución en sus diferentes canales de comunicación.Estas son:

-Facebook

-Twitter

-Instagram

# G)Reseñas:
Tal expresado en la seccion del Navbar, en esta pagina, vera usted todos los posteos realizados y guardados en la base de datos. Puede acceder a ellos mediante el hipervinculo con el titulo del articulo. Si usted esta logeado, podra editar y borrarlos, pero si no lo esta, le redirigira hacia la seccion de login.

En el texto, se le indicara algunas instrucciones de como mejorar la estructura de la reseña a crear.

# H)Fin:
Una vez que haya terminado de probar las diferentes funciones de la pagina, vuelva al vsc, haga click en la terminal y presione las teclas "Ctrl" + "C" para cerrar el servidor.

-Tambien se puede cerrar el servidor con cerrar el programa, que forzara el cierre de la aplicacion y la conexion con el servidor local.

Para ver el excel de casos de prueba + Video de presentación/tutorial, se encuentra en la siguiente carpeta de google drive:

(Recuerde que podra verlo y compartirlo, pero no podra editar el contenido, solo leer y comentarlo).

https://drive.google.com/drive/folders/1GSMwO7SPxjcCXyTkfdNddb_KHjxgpF1I?usp=sharing

A todo esto, se le agradece su visita y prueba del proyecto. muchas gracias por su atención.

Noir - Carranza - Smutt
