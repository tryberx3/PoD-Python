

**Patrón: Bridge**


**Descripción** <br>
Imagina que estás construyendo dos tipos de cosas: por un lado, tienes diferentes colores, como rojo, azul y verde; por otro lado, tienes diferentes formas, como círculos, cuadrados y triángulos. Quieres combinar estos colores y formas de manera flexible, ¡pero sin hacer un lío!

Aquí es donde entra en juego el patrón "Bridge". En lugar de tener un enredo de colores y formas juntos, divides las cosas en dos partes: una parte que trata con los colores y otra parte que trata con las formas. Estas dos partes pueden evolucionar por su cuenta sin depender una de la otra.

Y aquí está lo genial: cuando necesitas que un color se relacione con una forma específica, el patrón "Bridge" te permite hacerlo de manera ordenada. Imagina que tienes un círculo rojo. En lugar de tener una combinación especial para cada color y forma, el patrón "Bridge" te permite tener una relación entre el círculo y el color rojo sin crear un montón de combinaciones.

En resumen, el patrón de diseño "Bridge" es como tener dos equipos separados (uno para colores y otro para formas) que pueden trabajar juntos sin crear un lío. Te permite combinar cosas de manera flexible y ordenada, manteniendo las partes separadas y relacionándolas cuando sea necesario.

<br>

**Aplicabilidad**
- Abstracción y implementación independientes: Cuando tienes dos dimensiones de variación en tu sistema que pueden cambiar de manera independiente (como colores y formas), el patrón Bridge es útil. Te permite crear jerarquías separadas para cada dimensión y luego combinarlas de manera flexible.

- Evitar una explosión de subclases: Si tienes muchas combinaciones posibles de dos o más características y crearías una gran cantidad de subclases para cubrir todas las combinaciones, el patrón Bridge es beneficioso. Evita la necesidad de crear una subclase para cada combinación al usar composición en lugar de herencia.

- Apoyo a múltiples plataformas: Si estás desarrollando software que debe funcionar en múltiples plataformas (como diferentes sistemas operativos o dispositivos), el patrón Bridge es útil. Puedes tener una jerarquía para la plataforma y otra para las funcionalidades específicas, y luego combinarlas para crear versiones que funcionen en diferentes plataformas.

- Cambio y expansión sin afectar a otros componentes: Cuando necesitas agregar nuevas variantes de una característica sin afectar el resto del sistema, el patrón Bridge es una buena elección. Puedes introducir nuevas implementaciones y combinarlas con la abstracción existente sin alterar el código existente.