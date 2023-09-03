

**Patrón: Observer**

**Descripción:** <br>
El patrón de diseño "Observer" se trata de establecer una relación de "observador-sujeto" donde un objeto (llamado el "sujeto" o "observable") mantiene una lista de objetos interesados (llamados "observadores") y los notifica automáticamente cuando ocurren cambios en su estado.

Piensa en ello como seguir a alguien en las redes sociales. Cuando sigues a alguien, estás "observando" sus publicaciones. Cada vez que esa persona hace una nueva publicación, tú y otros seguidores reciben una notificación o actualización. De esta manera, puedes estar al tanto de lo que esa persona está haciendo sin tener que verificar constantemente su perfil.

En la programación, el patrón "Observer" se utiliza cuando tienes un objeto que cambia su estado con el tiempo y quieres que otros objetos se enteren de estos cambios sin necesidad de que los observadores estén constantemente verificando el estado del objeto. Los observadores se registran con el objeto sujeto y este les notifica automáticamente cuando ocurren cambios.

<br>

**Aplicabilidad**
- Cuando un objeto necesita notificar a varios objetos sin conocer sus identidades: El patrón Observer es útil cuando un objeto (sujeto u observable) necesita notificar a múltiples objetos (observadores) sobre cambios en su estado, pero no conoce cuáles son esos objetos de antemano. Los observadores se registran dinámicamente y pueden variar en número y tipo.

- Cuando un cambio en un objeto debe propagarse a otros objetos de manera automática: Si tienes un objeto cuyo cambio de estado debe ser conocido y procesado por otros objetos sin que el objeto sujeto tenga que comunicarse directamente con ellos, el patrón Observer facilita esta propagación automática de cambios.

- En implementaciones de eventos y manejo de eventos: En muchos sistemas de programación, como interfaces gráficas de usuario (GUI) o aplicaciones web, se utiliza el patrón Observer para manejar eventos y notificaciones. Los elementos de la interfaz gráfica (botones, cuadros de texto, etc.) actúan como observadores que responden a eventos como clics de botón.

- Cuando necesitas actualizar múltiples objetos en respuesta a un cambio: Si tienes una situación en la que un cambio en un objeto debe actualizar o sincronizar múltiples objetos en el sistema, el patrón Observer es una forma eficiente de lograr esto sin tener que gestionar manualmente las actualizaciones.

- En sistemas donde se requiere implementar un sistema de publicación-suscripción: El patrón Observer es fundamental para implementar sistemas de publicación-suscripción donde un editor (publicador) notifica a todos los suscriptores (observadores) sobre nuevos eventos o contenido.

- En aplicaciones de monitoreo y seguimiento: Si estás desarrollando aplicaciones que necesitan monitorear y rastrear cambios en tiempo real, como sistemas de vigilancia o sistemas de seguimiento de datos en tiempo real, el patrón Observer es muy útil para notificar a múltiples partes interesadas sobre eventos.