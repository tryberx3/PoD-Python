

**Patrón: Flyweight**


**Descripción:** <br>
El patrón de diseño estructural "Flyweight" trata sobre cómo ahorrar memoria o recursos al compartir partes comunes de objetos en lugar de replicarlas una y otra vez.

Piensa en ello como una forma de optimizar el uso de recursos cuando tienes muchas cosas que son parecidas pero que no necesitan ser completamente únicas.

Imagina que estás haciendo una aplicación de dibujo y necesitas representar miles de puntos en la pantalla. En lugar de crear un nuevo objeto para cada punto (que podría ser ineficiente en términos de memoria), puedes usar el patrón Flyweight. Esto significa que solo creas un objeto para un tipo de punto (digamos, un punto rojo) y lo reutilizas en todas partes donde necesites un punto rojo. Así, ahorras memoria y recursos al compartir objetos similares en lugar de crear uno nuevo cada vez.

En resumen, el patrón Flyweight se trata de ser eficiente al reutilizar partes comunes de objetos para ahorrar memoria o recursos cuando trabajas con muchas instancias similares. Es como tener un conjunto de bloques de construcción que puedes usar para construir muchas cosas en lugar de hacer cada una desde cero.

<br>

**Aplicabilidad**
- Cuando tienes un gran número de objetos similares: El patrón Flyweight es más efectivo cuando tienes una gran cantidad de objetos que comparten partes comunes y solo tienen pequeñas diferencias. En lugar de crear una instancia única para cada objeto, puedes compartir y reutilizar objetos similares, lo que ahorra memoria y recursos.

- Cuando la memoria o los recursos son limitados: Si estás desarrollando una aplicación que se ejecuta en un entorno con recursos limitados, como dispositivos móviles o sistemas embebidos, el patrón Flyweight puede ayudarte a optimizar el uso de memoria y recursos al reducir la duplicación de datos.

- Para mejorar el rendimiento: Al reducir la cantidad de objetos que necesitas crear y administrar, el patrón Flyweight puede mejorar significativamente el rendimiento de tu aplicación, especialmente en casos donde la creación de objetos es costosa en términos de tiempo y recursos.

- Cuando deseas separar datos intrínsecos y extrínsecos: El patrón Flyweight te permite separar los datos intrínsecos (comunes a varios objetos) de los datos extrínsecos (específicos de cada objeto). Esto puede simplificar tu diseño y hacer que tu código sea más modular.