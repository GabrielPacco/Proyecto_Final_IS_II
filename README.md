# Trabajo Final de Ingenieria de Software II: Pagina Web de eventos relacionados a computacion

## Proposito del Proyecto
Debido a los grandes avances y nuevas tecnologias relevantes para la sociedad de computacion que comprende entre investigadores, profesores, empresas, estudiantes y demas personas aficionados; esta pagina web pretende ser util para que los ponentes puedan notificar de sus proximos eventos a traves de una interfaz simple, y asi estos puedan mostrar mas interes a los temas tratados y agrandar la comunidad de ciencia de la computacion.

## Herramientas

-GitHub: Usamos este tipo de herramienta para crear un repositorio donde alojar nuestro proyecto.<br>
-JMeter<br>
-SonarQube: Es una plataforma para evaluar código fuente. Es software libre y usa diversas herramientas de análisis estático de código fuente como Checkstyle, PMD o FindBugs para obtener métricas que pueden ayudar a mejorar la calidad del código de un programa.<br>
-Sonar-scanner <br>
-JUnit: Es un conjunto de bibliotecas son utilizadas en programación para hacer pruebas unitarias de aplicaciones Java.JUnit es el estándar de facto para las pruebas unitarias de una aplicación Java. Aunque, es popular para las pruebas unitarias, tiene soporte completo y provisión para pruebas de instrumentación también. <br>
-OWASP ZAP <br>
-Selenium: Es un entorno de pruebas de software para aplicaciones basadas en la web. Selenium provee una herramienta de grabar/reproducir para crear pruebas sin usar un lenguaje de scripting para pruebas. <br>


# Análisis Estático


## Requisitos

### - Register

![alt text](Images/sign_up.png "Registrar")

### - Crear eventos

![alt text](Images/crear_evento_template.png "Crear evento")

### - Ver nuevos eventos

![alt text](Images/nuevos_eventos.png "Ver nuevos eventos")

  
## Github
Cada integrante ha creado su propia rama con su nombre sobre la cual ha trabajado y se ha realizado integracion continua sobre la rama de **desarrollo** en la cual se realizan las diferentes pruebas tanto unitarias, funcionales, de rendimiento, de seguridad y el analisis estatico.

![alt text](Images/github_branches.png "Github branches")

## Pipeline en Jenkins
Para realizar el procedimiento completo de integración continua es necesario trabajar con Jenkins. Por ello se ha creado un pipeline con el siguiente script
![](https://live.staticflickr.com/65535/52594947084_80b4c8d511_b.jpg)


## Construcción automática
En Python el tema de construcción automática no necesita de comandos específicos, pero si requiere un archivo requirements.txt el cual gaurdara todas las librerias usadas para el proyecto. Es necesario que para usarlo de forma correcta se use docker o un entorno virtual en python, de manera que solo se almacenen las librerias necesarias.

![alt text](Images/requirements.png "Requirements")

## Analisis Estático
-SonarQube official Plugin <br>
-SonarScanner Plugin <br>
-Sonar Qube Server <br>
-sonar-project.properties <br>

## Previsualización del análisis de Sonar Scanner

![image](https://github.com/GabrielPacco/Proyecto_Final_IS_II/blob/ronald/Images/Capturas_Sonar_Qube/localhost_9000_dashboard_id%3DProyecto_Final_IS_II_1.0(iPad%20Air).png) <br>
## Bugs
![image](https://github.com/GabrielPacco/Proyecto_Final_IS_II/blob/ronald/Images/Capturas_Sonar_Qube/Bugs.png) <br>

## Vulnerabilidades
![image](https://github.com/GabrielPacco/Proyecto_Final_IS_II/blob/ronald/Images/Capturas_Sonar_Qube/Security_Vulnerabilities.png) <br>

## Code Smells
![image](https://github.com/GabrielPacco/Proyecto_Final_IS_II/blob/ronald/Images/Capturas_Sonar_Qube/Code_Smells.png) <br>

## Refactoring Code

### FUNCIÓN INDEX

![](https://live.staticflickr.com/65535/52594725924_6f3d9e0c2a_b.jpg)

## Eliminación de código comentado

![](https://live.staticflickr.com/65535/52594898055_f2eca34e00_h.jpg)

## Arquitectura del proyecto: 

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
