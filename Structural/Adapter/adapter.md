

**Patrón: Adapter**


**Descripción** <br>
El patrón de diseño estructural "Adapter" se trata de hacer que dos interfaces incompatibles puedan trabajar juntas. Es como usar un adaptador para conectar dos cosas que no encajarían de otra manera.

Piensa en ello como enchufar un dispositivo eléctrico a una toma de corriente de un país extranjero. El enchufe del dispositivo no encaja directamente en la toma de corriente, pero puedes usar un adaptador que se conecta al enchufe del dispositivo y lo hace compatible con la toma de corriente.

En programación, el patrón "Adapter" hace algo similar. Permite que dos clases o componentes con interfaces diferentes trabajen juntas. Un adaptador actúa como un intermediario que toma las solicitudes de una interfaz y las traduce en algo que la otra interfaz pueda entender.

Entonces, en resumen, el patrón "Adapter" se trata de hacer que dos cosas incompatibles funcionen juntas mediante la creación de un intermediario que traduzca las solicitudes de una interfaz en algo que la otra interfaz pueda entender. Es como usar un adaptador para conectar un enchufe a una toma de corriente que no es compatible de forma directa.

<br>

**Aplicabilidad**
- Cuando necesitas hacer que clases existentes sean compatibles: El patrón Adapter es útil cuando tienes una clase (o interfaz) existente con una interfaz incompatible que necesitas que funcione con otras clases o componentes que esperan una interfaz diferente.

- Integración de bibliotecas o componentes de terceros: Si estás utilizando una biblioteca o un componente de terceros que tiene una interfaz que no se adapta directamente a tus necesidades, puedes crear un adaptador para hacer que funcione con tu código existente.

- Reutilización de código heredado: Cuando estás trabajando con código heredado que no se puede modificar fácilmente, el patrón Adapter te permite interactuar con él desde el nuevo código sin tener que realizar cambios significativos en el código heredado.

- Cuando deseas abstraer y desacoplar sistemas: El Adapter puede ayudarte a desacoplar sistemas, ya que permite que los sistemas interactúen a través de una interfaz común, lo que facilita la sustitución de componentes y la modularidad.

- Cuando trabajas con interfaces incompatibles en sistemas distribuidos: En sistemas distribuidos, es común que los servicios tengan interfaces incompatibles. Un Adapter puede servir como un punto de entrada uniforme para interactuar con múltiples servicios.

- Mejorar la legibilidad y mantenibilidad: El patrón Adapter puede mejorar la legibilidad de tu código al ocultar la complejidad de la adaptación entre interfaces, lo que hace que el código sea más claro y fácil de mantener.

- Cuando deseas encapsular una clase compleja: Puedes usar un Adapter para encapsular una clase compleja y proporcionar una interfaz más simple y específica para su uso.

- Para agregar funcionalidad adicional a una clase existente: Puedes crear un Adapter que envuelva una clase existente y agregue funcionalidad adicional o modifique su comportamiento sin modificar la clase original.