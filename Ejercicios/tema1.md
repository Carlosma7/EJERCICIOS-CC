# Ejercicios de autoevaluación tema 1 - Cloud Computing.

### 1- Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?

La aplicación que voy a utilizar de ejemplo se llama **Napakalaki**, la cual consiste en un juego de cartas desarrollado a lo largo del grado en ingeniería informática. Esta aplicación que realicé en la asignatura de *PDOO* se puede encontrar [aquí](https://github.com/Carlosma7/PDOO), tanto en su versión en *Java* como en *Ruby*. 

El patrón utilizado para el desarrollo de esta aplicación consiste en una arquitectura **MVC** (Modelo Vista Controlador), en las cuales se distinguen los distintos componentes de la aplicación como tres grandes bloques que interactuan. Para llevar esta arquitectura a un patrón del tipo microservicios sería necesario analizar los distintos servicios que ofrece la aplicación, para realizar dichos servicios de forma independiente y que se comunicaran entre ellos, como podrían ser: Gestión de jugadores, Pelea entre cartas, Interacción entre el jugador y sus cartas, etc.

### 2- En la aplicación que se ha usado como ejemplo en el ejercicio anterior, ¿podría usar diferentes lenguajes? ¿Qué almacenes de datos serían los más convenientes?

La aplicación se realizó en su día en dos lenguajes diferentes como son *Java* y *Ruby*, por lo que se podrían emplear distintos lenguajes según las distintas necesidades o conveniencias que pudieran surgir en cada uno de los microservicios a realizar. De esta forma cada microservicio se podría realizar de forma independiente al resto con el lenguaje más conveniente, sin necesidad de una dependencia de lenguaje sobre el que desarrollarse.

Por otro lado, al tratarse de un juego de cartas, realmente no supondría un problema utilizar cualquier tipo de almacén de datos. Inicialmente se plantearía un almacén tradicional, relacional y de tipo SQL, debido a que la información que manejamos son cartas. Todos los elementos del juego estarían bien definidos y conocemos sus características y relaciones de antemano. Esto a su vez, no implica que no podamos utilizar otro tipo de almacén de datos si nos plantearamos añadir otras funcionalidades nuevas que implicaran cambios en el concepto del juego.
