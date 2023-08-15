

**Patrón: Prototype**


**Descripción** <br>
Imagina que estás haciendo galletas. Cuando haces una galleta, utilizas una plantilla (un molde) para darle forma a la masa. Ahora, en el mundo de la programación, el patrón "Prototype" es similar a esto.

En lugar de crear objetos desde cero cada vez que los necesitas, el patrón "Prototype" te permite crear una especie de "molde" (prototipo) de un objeto. Luego, cuando necesitas un objeto nuevo, en lugar de hacerlo desde cero, simplemente haces una copia del prototipo y lo ajustas según lo necesites.

Es como si tuvieras una receta básica para un objeto y, en lugar de cocinar desde cero cada vez, simplemente duplicas esa receta y haces algunos ajustes si es necesario. Esto ahorra tiempo y esfuerzo en la creación de objetos similares.

<br>

**Aplicabilidad**
- Creación de objetos costosa: Cuando la creación de un objeto es costosa en términos de recursos o tiempo, y necesitas crear objetos similares con frecuencia, el patrón Prototype puede ser útil. En lugar de crear nuevos objetos desde cero cada vez, puedes clonar un prototipo existente, lo que puede ser más eficiente.

- Configuraciones iniciales variadas: Si tienes objetos que comparten una estructura común pero difieren en sus configuraciones iniciales, el patrón Prototype es útil. Puedes crear un prototipo con la estructura común y luego clonar ese prototipo para crear objetos con diferentes configuraciones.

- Evitar subclases múltiples: Si estás pensando en crear múltiples subclases de una clase para representar diferentes variantes de un objeto, el patrón Prototype puede ser preferible. En lugar de crear una jerarquía de subclases, puedes tener un prototipo base y crear variantes clonando ese prototipo.

- Aplicaciones que requieren copias exactas: En algunos casos, necesitas copias exactas de objetos para garantizar que no haya efectos secundarios no deseados. El patrón Prototype garantiza que obtengas copias profundas y exactas de los objetos, lo que puede ser crítico en aplicaciones sensibles.