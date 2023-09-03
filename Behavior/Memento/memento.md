

**Patrón: Memento**

**Descripción:** <br>
el patrón de diseño "Memento" trata sobre capturar y guardar el estado interno de un objeto en un momento específico, de manera que puedas restaurar ese estado más tarde si es necesario. Es como tomar una "foto" de un objeto para poder volver a ese estado en el futuro.

Imagina que estás jugando a un videojuego y quieres guardar tu progreso. Usas una opción de "guardar partida" para crear un punto de control. Si más tarde decides cargar esa partida guardada, el juego te devuelve exactamente al mismo lugar y con el mismo inventario que tenías en ese momento.

El patrón "Memento" es como esa función de guardar y cargar en un videojuego. Te permite guardar el estado de un objeto, como valores de sus atributos, y luego restaurar ese estado en el futuro si es necesario. Esto es útil cuando quieres permitir que los usuarios o el sistema puedan deshacer acciones o volver a estados anteriores en una aplicación.

<br>

**Aplicabilidad**
- Cuando necesitas implementar la funcionalidad de deshacer (undo) en una aplicación: El patrón Memento es especialmente útil para permitir a los usuarios deshacer acciones previas y restaurar un estado anterior de la aplicación. Guardar instantáneas del estado en momentos clave facilita la implementación de esta función.

- Cuando debes capturar y restaurar el estado de un objeto o una aplicación en diferentes puntos: Si tu aplicación necesita capturar el estado de un objeto o sistema en varios puntos y luego restaurar ese estado en un momento posterior, el patrón Memento es apropiado.

- En editores de texto o aplicaciones de diseño gráfico: En aplicaciones donde los usuarios trabajan con contenido creativo, como editores de texto o gráficos, el patrón Memento puede utilizarse para guardar versiones históricas del contenido y permitir que los usuarios vuelvan a estados anteriores.

- En juegos y simulaciones: En juegos y simulaciones complejas, el patrón Memento se usa para guardar y cargar estados de juego, lo que permite a los jugadores retomar el juego desde un punto anterior.

- En aplicaciones de configuración y preferencias: Si tu aplicación permite a los usuarios configurar preferencias o estados personalizados, el patrón Memento puede utilizarse para guardar y restaurar estas configuraciones.

- En sistemas de respaldo y recuperación: En sistemas que requieren la capacidad de realizar copias de seguridad y recuperar datos, el patrón Memento se utiliza para almacenar instantáneas de datos en diferentes momentos.

- En aplicaciones de historial de navegación: En navegadores web y aplicaciones similares, el patrón Memento se usa para rastrear el historial de navegación y permitir que los usuarios vuelvan a páginas web visitadas previamente.