#Programacion Orientada a Objetos

## Descripcion del problema
Este programa hace uso de caracteristicas de la POO, como herencia, metodos, encapsulamiento, clases y objetos. Es demostrativo.

## Especificación de Requisitos
Requisitos no funcionales:

Script en Python 
Tiempo de respuesta rapido

## Análisis y Diseño

### Superclase Animal:

Define los atributos nombre y edad en el constructor (__init__).
Define el método abstracto haz_ruido para ser sobrescrito por las subclases.
Define el método abstracto to_dict para ser sobrescrito por las subclases.
Clase Perro:

### Hereda de Animal.
Implementa el método haz_ruido para retornar "Guau".
Implementa el método to_dict para retornar un diccionario con tipo, nombre, edad, y onomatopeya.
Clase Gato:

### Hereda de Animal.
Añade el atributo usa_arenero en el constructor.
Implementa el método haz_ruido para retornar "Miau".
Implementa el método to_dict para retornar un diccionario con tipo, nombre, edad, usa_arenero, y onomatopeya.
Demostración de Funcionalidad:

### Se crean instancias de Perro y Gato.
Se imprime la información directamente.
Se accede a la información a través del método to_dict y se imprime.