

**Patrón: State**

**Descrición:** <br>
El patrón de diseño "State" se trata de permitir que un objeto cambie su comportamiento cuando su estado interno cambia. Piensa en ello como si una máquina pudiera comportarse de manera diferente dependiendo de su estado actual.

Para explicarlo más simple, imagina una máquina expendedora de bebidas. Esta máquina puede tener diferentes estados, como "Esperando selección", "Vendiendo producto" y "Sin cambio disponible". Dependiendo de su estado actual, la máquina tomará acciones diferentes cuando un usuario inserte dinero o haga una selección. Si está en el estado "Esperando selección", tomará la orden del usuario, pero si está en el estado "Sin cambio disponible", mostrará un mensaje de error.

El patrón "State" organiza estos diferentes estados en clases separadas y permite que el objeto cambie su estado interno y, por lo tanto, su comportamiento, en tiempo de ejecución. Esto hace que el código sea más flexible y fácil de mantener, ya que puedes agregar nuevos estados o cambiar el comportamiento de un estado existente sin tener que modificar el objeto principal.

<br>

**Aplicabilidad**
Cuando un objeto debe cambiar su comportamiento en función de su estado interno: Si tienes un objeto que debe realizar acciones diferentes en función de su estado actual, el patrón State es útil. Por ejemplo, una máquina que se comporta de manera diferente cuando está encendida, apagada o en modo de espera.

Cuando deseas que tu código sea más modular y fácil de mantener: El patrón State promueve la encapsulación de comportamientos relacionados en clases separadas, lo que hace que tu código sea más modular y más fácil de entender y mantener. Puedes agregar nuevos estados o modificar el comportamiento de un estado existente sin afectar el resto del código.

Cuando tienes múltiples estados y transiciones entre ellos: Si tu objeto tiene una serie de estados y las transiciones entre ellos son complejas, el patrón State puede simplificar la gestión de esas transiciones y mejorar la legibilidad del código.

Cuando trabajas en un proyecto que necesita ser altamente flexible y extensible: El patrón State facilita la adición de nuevos estados y la modificación del comportamiento del objeto sin alterar el código existente, lo que lo hace adecuado para proyectos que deben ser altamente adaptables a cambios futuros.

En sistemas que necesitan comportamientos personalizables: Si trabajas en sistemas donde los usuarios pueden personalizar o configurar el comportamiento de objetos, el patrón State permite agregar fácilmente nuevos estados personalizados.

Cuando necesitas implementar una máquina de estados: El patrón State es fundamental para diseñar máquinas de estados en aplicaciones como controladores de dispositivos, juegos y sistemas de automatización.