

**Patrón: Facade**


**Descripción:** <br>
Imagina que estás tratando de encender una computadora. En lugar de abrir la computadora y tocar cada componente individualmente, simplemente presionas el botón de encendido. Ese botón es como una interfaz sencilla que oculta la complejidad interna de la computadora y te permite realizar una acción con un solo paso.

El patrón "Facade" en la programación es algo similar. Proporciona una interfaz simplificada para un conjunto más grande y complejo de componentes. En lugar de tratar directamente con todos los detalles internos, puedes interactuar con una interfaz "facade" que oculta la complejidad y simplifica la interacción.

<br>

**Aplicabilidad**
- Sistema complejo con múltiples subsistemas: Cuando estás trabajando con un sistema complejo que consta de varios subsistemas o componentes interconectados, y deseas proporcionar una interfaz más simple y unificada para interactuar con todo el sistema. El patrón Facade actúa como un punto de entrada único para el cliente.

- Ocultar detalles de implementación: Cuando deseas ocultar los detalles de implementación de un sistema complejo o de un conjunto de clases para evitar que el cliente acceda directamente a ellos. Esto puede ser útil para mantener una capa de abstracción y permitir cambios internos sin afectar al cliente

- Mejorar la legibilidad y el mantenimiento: Si tienes un código que se ha vuelto difícil de entender debido a su complejidad y la interacción con múltiples clases o subsistemas, el patrón Facade puede mejorar la legibilidad al proporcionar una interfaz más clara y declarativa.