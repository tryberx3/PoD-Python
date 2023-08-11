

**Patró: Builder**


**Descripción**
El patrón de diseño creacional "Builder" se trata de crear objetos complejos paso a paso. Imagina que estás construyendo una casa. En lugar de construir toda la casa de una vez, primero construyes las partes más pequeñas, como las paredes, el techo y las ventanas, y luego las ensamblas para formar la casa completa.

En el patrón Builder, hay dos partes clave: el "Builder" (constructor) y el "Director". El constructor es responsable de construir cada parte del objeto de manera individual, mientras que el director coordina la secuencia en la que se ensamblan las partes.

En resumen, el patrón Builder se trata de dividir la creación de un objeto complejo en pasos más pequeños y manejables. Esto hace que el proceso sea más flexible, ya que puedes crear diferentes tipos de objetos combinando diferentes partes. Además, separa la construcción del objeto de su representación final, lo que facilita la creación de objetos complejos sin complicar el código.


**Aplicabilidad**
- Creación de objetos complejos: Cuando necesitas crear objetos complejos que constan de múltiples partes y configuraciones, el patrón Builder puede ayudarte a separar el proceso de construcción del objeto final del código cliente.

- Evitar constructores telescópicos: Cuando una clase tiene muchos parámetros en su constructor, es difícil de mantener y propenso a errores. El patrón Builder permite dividir la construcción en etapas más manejables y legibles.

- Varios tipos de objetos: Si tu aplicación necesita construir diferentes tipos de objetos que comparten algunas características comunes pero tienen variaciones, el Builder permite crear múltiples constructores que implementen una interfaz común.

- Producción en serie: Si necesitas crear varios objetos con configuraciones similares, el Builder puede reducir la repetición de código y mejorar la reutilización al definir constructores con diferentes configuraciones.

- Ocultar detalles de implementación: El patrón Builder puede ocultar los detalles internos de cómo se construye un objeto. Esto puede ser útil cuando no deseas exponer todos los detalles de construcción al código cliente.

- Facilitar el testing: Al separar la construcción de un objeto de su uso, puedes crear pruebas más eficientes alrededor de los constructores, asegurando que los objetos se creen correctamente y con las configuraciones adecuadas.

- Adición de nuevas configuraciones: Si anticipas la necesidad de agregar nuevas configuraciones o características en el futuro, el Builder permite extender los constructores existentes sin afectar el código cliente.