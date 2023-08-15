

**Patrón: Proxy**


**Descripción** <br>
Imagina que tienes una persona famosa que solo quiere hablar con personas cercanas y de confianza. Ahora, en el mundo de la programación, el patrón "Proxy" es un poco similar a esto.

El patrón "Proxy" es como un amigo o asistente que actúa como intermediario entre tú y algo más, como un objeto o servicio. Si quieres hablar con ese objeto o servicio, primero hablas con el "Proxy", y luego el "Proxy" se encarga de transmitir tus solicitudes.

Este amigo o asistente (el "Proxy") puede hacer algunas cosas interesantes, como verificar si tienes permiso para acceder al objeto o servicio, cargarlo solo cuando realmente lo necesitas, o hacer algunas tareas adicionales antes o después de que hables con el objeto o servicio real.

En resumen, el patrón de diseño "Proxy" te permite tener un intermediario que controla el acceso y las interacciones con un objeto o servicio. Es como tener a alguien de confianza entre tú y lo que quieres hacer, ¡y puede hacer algunas cosas útiles por ti!

<br>

**Aplicabilidad**
- Control de acceso: Cuando necesitas controlar el acceso a un objeto, ya sea para verificar permisos, autenticar usuarios o limitar el acceso en función de ciertas condiciones, el patrón Proxy es útil. El proxy puede manejar la lógica de acceso antes de permitir que el cliente interactúe con el objeto real.

- Carga perezosa (Lazy loading): Si tienes objetos costosos de crear o inicializar, como imágenes grandes o bases de datos, el patrón Proxy es beneficioso. El proxy puede cargar el objeto real solo cuando sea necesario, evitando la carga innecesaria y mejorando el rendimiento.

- Referencias remotas: En sistemas distribuidos o de red, el patrón Proxy puede utilizarse para representar objetos remotos. El proxy actúa como intermediario que maneja la comunicación con el objeto remoto, lo que permite al cliente acceder al objeto como si estuviera local.

- Cacheo: Si deseas mejorar el rendimiento almacenando en caché resultados previos, el patrón Proxy es adecuado. El proxy puede almacenar en caché los resultados de operaciones costosas y devolverlos directamente en lugar de recalcularlos cada vez.

- Logging o auditoría: Si necesitas llevar un registro de las acciones realizadas en un objeto o mantener un registro de auditoría, el patrón Proxy puede ser útil. El proxy puede registrar las interacciones antes de pasarlas al objeto real.

- Optimización de recursos: Cuando deseas limitar el número de instancias de objetos creadas para optimizar el uso de recursos, el patrón Proxy puede ser aplicado. El proxy puede gestionar la creación y liberación de objetos según la demanda.