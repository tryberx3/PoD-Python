

**Patrón: Singleton**

**Descripción** <br>
El patrón Singleton es un patrón de diseño que asegura que solo exista una única instancia de una clase en toda la aplicación.

Piensa en ello como tener una caja de galletas que todos comparten. Si un cliente quiere galletas, toma de la misma caja que otros clientes. Si se intenta crear una nueva caja, en realidad solo se obtiene la misma caja existente.

En la programación, esto se aplica cuando quieres asegurarte de que solo haya una única instancia de una clase en tu programa. Esto puede ser útil para compartir información o recursos entre diferentes partes de tu programa sin tener duplicados innecesarios. Por ejemplo, si tienes una clase que maneja una conexión a una base de datos, querrías asegurarte de que solo haya una instancia para evitar problemas.

<br>

**Aplicabilidad**
- Acceso a una única instancia global: Cuando necesitas acceder a una instancia única desde múltiples partes de tu aplicación, como una conexión a la base de datos, un registro de eventos o un administrador de configuración.

- Recursos compartidos: Si tienes recursos costosos en términos de rendimiento o recursos, como conexiones a bases de datos o manejo de archivos, el patrón Singleton garantiza que solo haya una instancia que administre estos recursos.

- Configuración global: Cuando deseas mantener una configuración global consistente para toda la aplicación, como la configuración del sistema, opciones de estilo o preferencias del usuario.

- Control de acceso: Puede utilizarse para controlar el acceso concurrente a ciertos recursos o componentes compartidos.

- Caché: En situaciones en las que necesitas mantener una caché de datos o resultados, el patrón Singleton puede ayudar a administrar la caché y garantizar que se comparta adecuadamente.

- Logging y seguimiento: Para administrar registros y seguimiento en toda la aplicación, asegurando que los mensajes de registro no se mezclen entre múltiples instancias.

- Gestión de conexiones: En sistemas que manejan conexiones a API externas, sistemas de terceros o servicios web, el Singleton puede ayudar a gestionar eficientemente estas conexiones.

- Componentes que requieren un estado compartido: Cuando tienes componentes que necesitan compartir un estado global, como administradores de estado en aplicaciones frontend.