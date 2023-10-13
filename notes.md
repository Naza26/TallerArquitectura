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