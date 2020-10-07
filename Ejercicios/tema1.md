# Ejercicios de autoevaluación tema 1 - Cloud Computing.

### 1- Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?

La aplicación a desarrollar va a consistir en una plataforma de Freelance, donde podemos buscar ofertas de proyectos, contratación a trabajadores autónomos o Freelance. En dicha aplicación, los distintos trabajadores podrán buscar proyectos, y las empresas u organizaciones podrán ofertar y seleccionar distintos profesionales para la realización de tareas mediante subcontrataciones.

En un principio, esta idea se plantea como una aplicación con una arquitectura por capas, la cual consiste de tres capas de presentación, lógica de negocio y base de datos. Para pasar de dicha arquitectura a un patrón del tipo microservicios, deberíamos distinguir las distintas funcionalidades que se ofertan en la aplicación, distinguiendo servicios como:

* Gestión peticiones REST
* Gestión de usuarios
* Gestión de BD
* Microservicio de búsqueda de especialistas según cualidades
* Microservicio de búsqueda de proyectos según ámbito profesional

### 2- En la aplicación que se ha usado como ejemplo en el ejercicio anterior, ¿podría usar diferentes lenguajes? ¿Qué almacenes de datos serían los más convenientes?

