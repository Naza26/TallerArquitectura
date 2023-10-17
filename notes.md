Aprendizaje, decisiones de disenio

## Tarea 00 - Seteo del entorno de trabajo

- Familiarizacion con el entorno de trabajo
- Intellij como IDE
- Proyectos, modulos, dependencias

## Tarea 01 - Funcionalidad del Negocio

### Objetivo
- Alcance
- Programar con TDD el negocio
- Modelar las restricciones
- Asignar las responsabilidades de dónde viven las restricciones
- Modelar la funcionalidad del sistema (cómo se puede usar el sistema)
- Cuidar la consistencia del sistema:
  - Cuidar que no entre nada corrupto al sistema 
  - Cuidar que la salida no permita la corrupción del sistema 
  - Afuera: objetos planos (la mayoría de las veces), Adentro: objetos de negocio
- Resolver cómo desde afuera se referencian objetos del sistema

### Fuera del alcance
- Sin persistencia
- Manejo de errores 
- Resolver cuestiones de protocolo (http o línea de comandos)
- Interactuar/utilizar el framework de comunicación (Django en este caso)

### Mi input, mi iteración

¿Cómo modelaron los textos y títulos válidos?
- Cada test hardcodea en variables los textos y titulos validos

¿Qué objetos de negocio modelaron?

- Magazine
- Article

¿Dónde se crea el artículo?
- Se crea afuera de la Magazine y luego se lo agrega

¿Dónde está la responsabilidad de que un artículo sea válido?
- Se valida cuando se agrega/publica en la Magazine aunque tuve conflicto con esta decision ya que yo queria que se cree como un objeto completo y valido. Sin embargo, tome la decision de que la revista sea la responsable de validar que el articulo sea valido o no ya que a priori, parecia lo mas adecuado y simple de programar.

¿Y los valores de los límites, cómo los modelaron?
- En constantes en un objeto de negocio

¿Por qué no le pasamos un Article creado al dar de alta uno en el sistema?
- Porque me pude permitir corromper el sistema

¿Cómo reciclamos textos y títulos válidos?
- Referencié a los tests. Me hizo mucho ruido tener mucho código repetido entre magazine system y magazine tests por lo que trate de reutilizar el catalogo de articulos y titulos validos que ya tenia en los tests.

¿Cómo resolvemos poder referenciar un artículo desde afuera del sistema? Recordemos que desde afuera favorecemos no tener objetos del sistema, en pos de tener objetos inmutables, planos y/o literales
- Yo pensé en asociar cada articulo a un ID que lo identifica univocamente. Es la magazine la que se encarga de asignarle un ID al articulo cuando se lo agrega. De esta manera, desde afuera se puede referenciar al articulo por su ID. Sin embargo, haber hecho este cambio me generó una complejidad innecesario en la serializacion de los objetos planos y los objetos de negocio que yo creo que introduce una complejidad accidental cuando se quiere acceder a un articulo en cuestion.
Ademas, siento que estoy perdiendo declaratividad y conceptualidad. En la magazine, ya no tengo solamente articulos, ahora tengo un diccionario con un id:articulo. Siento que falta reificar algo, porque me hace mucho ruido querer recorrer los articulos de la magazine y estar descomponiendo ese id y los articulos. Siento que el id, es la mejor solucion, pero no lo dejé prolijo, algo falta.
Lo pensé y el id no tiene que ser propio de cada articulo, es acorde que cada revista tenga su conjunto de articulos con sus respectivos ids.

¿Qué problemas tuvieron que resolver? ¿Estos problemas aparecen también en sus sistemas “normales” o comerciales? En caso de que si, ¿en dónde los resuelven?
- El problema que mencioné en la pregunta anterior, esto me apareció desde el lado de system, cuando tuve que modelar esta capa entre objetos planos (exterior) y objetos de negocio (interior)

