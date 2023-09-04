

**Patrón: Chain of Responsibility**

**Descrioción:** <br>
El patrón de diseño "Chain of Responsibility" (Cadena de Responsabilidad) trata sobre pasar una solicitud a través de una serie de objetos que pueden manejarla o pasarla a otro objeto en la cadena. Es como cuando tienes un problema y primero le preguntas a una persona si puede ayudarte. Si esa persona no puede resolverlo, preguntas a otra persona, y así sucesivamente, hasta que alguien puede resolver tu problema o llegas al final de la lista de personas.

En términos más simples, imagina una cadena de objetos, como una cadena de montañas. Cada montaña en la cadena puede decidir si puede o no escalarla. Si una montaña no es adecuada para escalar, pasas a la siguiente en la cadena. Así, continúas hasta que encuentras una montaña que puedes escalar o llegas al final de la cadena.

El patrón "Chain of Responsibility" se utiliza para lograr un desacoplamiento flexible entre objetos que procesan solicitudes. Cada objeto en la cadena decide si puede manejar la solicitud o si debe pasarla al siguiente objeto en la cadena. Esto permite que las solicitudes se procesen de manera dinámica y modular, sin necesidad de que el remitente de la solicitud conozca en detalle quién la manejará.

<br>

**Aplicabilidad**
- Cuando tienes múltiples objetos que pueden manejar una solicitud: Si en tu programa tienes varios objetos o componentes que pueden manejar una solicitud o acción, y no quieres que el remitente de la solicitud esté fuertemente acoplado a estos objetos, el patrón Chain of Responsibility es útil.

- Cuando deseas dar a varios objetos la oportunidad de procesar una solicitud: El patrón permite que múltiples objetos intenten manejar una solicitud en orden hasta que uno de ellos lo haga. Esto es útil cuando quieres dar a varios objetos la oportunidad de procesar la solicitud antes de decidir cómo se manejará.

- Cuando necesitas aplicar comportamientos condicionales en secuencia: Si tienes una serie de condiciones que deben cumplirse secuencialmente, el patrón Chain of Responsibility te permite organizar estas condiciones en una cadena de objetos que procesen la solicitud una tras otra.

- Cuando deseas agregar o eliminar responsabilidades de manera dinámica: El patrón Chain of Responsibility facilita la adición o eliminación de manejadores de solicitudes sin afectar al remitente ni a otros manejadores existentes.

- En sistemas de manejo de eventos o middleware: El patrón se usa comúnmente en sistemas que manejan eventos, middleware de comunicación, procesamiento de solicitudes HTTP y en situaciones donde múltiples componentes pueden tomar medidas sobre un evento o solicitud.

- Cuando tienes una jerarquía de objetos con diferentes niveles de manejo: Si tus objetos forman una jerarquía en la que algunos pueden manejar solicitudes a niveles más altos o bajos, el patrón Chain of Responsibility es apropiado para organizar esta jerarquía de manejo.