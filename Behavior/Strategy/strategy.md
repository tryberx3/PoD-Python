

**Patrón: Strategy**

**Descripción:** <br>
el patrón de diseño "Strategy" se trata de poder cambiar el comportamiento de una parte de tu programa sin tener que cambiar todo el código. Imagina que estás jugando a un videojuego y puedes elegir diferentes estrategias para enfrentar a tus enemigos.

En términos más simples, el patrón "Strategy" te permite definir una familia de algoritmos, encapsular cada uno de ellos en una clase diferente y hacer que sean intercambiables. Esto significa que puedes cambiar la estrategia que se utiliza en tiempo de ejecución sin tener que modificar el código que la utiliza.

Por ejemplo, en un programa de procesamiento de imágenes, podrías tener diferentes estrategias para aplicar filtros a una imagen. Puedes cambiar la estrategia de filtro sin tener que reescribir todo el programa, simplemente seleccionas la estrategia que deseas utilizar en ese momento.

<br>

**Aplicabilidad**
- Cuando tienes varias formas de realizar una tarea: Si tu programa tiene una tarea que puede realizarse de varias formas diferentes o con algoritmos alternativos, el patrón Strategy es útil. Te permite encapsular cada estrategia en una clase separada y seleccionar la estrategia adecuada en tiempo de ejecución.

- Cuando deseas evitar un código duplicado: Si encuentras que tienes código duplicado en tu programa debido a diferentes variantes de una tarea, el patrón Strategy puede ayudarte a eliminar la duplicación al permitir que las estrategias compartan una interfaz común.

- Cuando quieres mejorar la flexibilidad y la reutilización del código: El patrón Strategy promueve la flexibilidad al permitir que elija la estrategia en tiempo de ejecución. Además, facilita la reutilización de las estrategias en diferentes partes de tu programa.

- En situaciones donde el comportamiento debe ser intercambiable: Si necesitas que el comportamiento de una parte de tu programa sea intercambiable en tiempo de ejecución, como en configuraciones dinámicas o preferencias de usuario, el patrón Strategy es adecuado.