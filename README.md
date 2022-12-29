# Trabajo Final de Ingenieria de Software II: Pagina Web de eventos relacionados a computacion

## Proposito del Proyecto
Debido a los grandes avances y nuevas tecnologias relevantes para la sociedad de computacion que comprende entre investigadores, profesores, empresas, estudiantes y demas personas aficionados; esta pagina web pretende ser util para que los ponentes puedan notificar de sus proximos eventos a traves de una interfaz simple, y asi estos puedan mostrar mas interes a los temas tratados y agrandar la comunidad de ciencia de la computacion.

## Funcionalidades
La pagina web presenta entre sus principales funcionalidades:

### - Visualizar a traves de una interfaz grafica eventos relacionados a la computacion

![alt text](Images/interfaz.PNG "Title")

### - Obtener mas informacion de los eventos

![alt text](Images/eventos.PNG "Title")

### - Acceder a los perfiles de los ponentes

![alt text](Images/perfil.PNG "Title")

### - Interaccion a traves de sesiones

![alt text](Images/login.PNG "Title")


Arquitectura del proyecto: 

### Interface
Esta capa contiene todo lo que interactúa con otros sistemas, como los servicios web, las interfaces RMI o las aplicaciones web, y los frontales de procesamiento por lotes. Se encarga de la interpretación, validación y traducción de los datos entrantes. También se encarga de la serialización de los datos salientes, como HTML o XML a través de HTTP para los navegadores web o los clientes de servicios web.

### Application
La capa de aplicación se encarga de dirigir el flujo de trabajo de la aplicación en función de los casos de uso que se presentaron.
Estas operaciones son independientes de la interfaz y pueden ser tanto sincrónicas como basadas en señales. Esta capa es muy adecuada para abarcar las transacciones, el registro de alto nivel y la seguridad.

La capa de aplicación es poco exigente en cuanto a la lógica de dominio: se limita a coordinar los objetos de la capa de dominio para realizar el trabajo real.

### Domain
La capa de dominio es el corazón del software, es el núcleo de la lógica de negocio.
Aqui se realizan tareas como determinar si un evento de manipulación debe ser registrado y cómo la entrega de una carga se ve afectada por la manipulación.

La estructura y la denominación de los agregados, las clases y los métodos de la capa deberían seguir el lenguaje del grupo, y cualquier miembro debería ser capaz de explicar a un experto en el dominio cómo funciona cierta parte del software dibujando unos cuantos diagramas sencillos y utilizando los nombres reales de las clases y los métodos del código fuente.

## Integrante (en orden alfabetico):

-Diego Josue Aquino Quispe <br>
-Erick Jesus Perez Chipa <br>
-Gabriel Pacco Huaraca <br>
-John Edson Sanchez Chilo <br>
-Levi Joel Castillon Urquiza <br>
-Ronald Romario Gutierrez Arratia  <br>



© Copyright 2022 All rights reserved
