# FASTA FRAMES

## Descripcion del problema
El programa toma una secuencia de ADN en formato FASTA desde un archivo especificado por el usuario. Luego, para cada uno de los seis marcos de lectura posibles (tres en la cadena directa y tres en la cadena complementaria), extrae los codones de la secuencia y los guarda en archivos separados en formato FASTA, nombrados como Frame1.fasta, Frame2.fasta, ..., Frame6.fasta.

## Especificacion de Requisitos 
### Funcionales
* Capacidad de leer archivos en formato FASTA
* Lenguaje de programacion (Python)
* Disponibilidad de BioPython 
* Disponibilidad de argparse
* Eficencia y rapidez

## Analisis y diseño
1. Importaciones:

Importamos argparse para manejar los argumentos de la línea de comandos.
Importamos las clases necesarias de BioPython (Seq para manejar secuencias de ADN y SeqIO para leer archivos FASTA).

2. Función extract_codons:

Esta función toma tres parámetros: frame (el marco de lectura), sequence (la secuencia de ADN) y output_filename (el nombre del archivo de salida en formato FASTA).
Si el marco de lectura es 3 o más, significa que estamos trabajando con la cadena complementaria inversa, así que ajustamos la secuencia en consecuencia.
Luego, extraemos los codones de la secuencia en el marco de lectura específico y los guardamos en el archivo de salida en formato FASTA.

3. Función main:

Creamos un objeto ArgumentParser de argparse para manejar el argumento de línea de comandos que representa la ruta al archivo de entrada (input_file).
Leemos la secuencia de ADN desde el archivo especificado por el usuario usando SeqIO.read.
Llamamos a extract_codons para cada uno de los 6 marcos de lectura, generando archivos FASTA para cada marco.
Imprimimos un mensaje confirmando que los codones se han guardado en los archivos correspondientes.
Ejecución desde la línea de comandos:

El programa espera que se le pase la ruta al archivo de entrada que contiene la secuencia de ADN en formato FASTA como un argumento de línea de comandos.
El usuario ejecuta el programa desde la terminal proporcionando la ruta al archivo de entrada como un argumento.

4. Manejo de la secuencia:

La secuencia de ADN se lee del archivo FASTA proporcionado por el usuario.
BioPython se utiliza para manejar la secuencia de ADN y los archivos en formato FASTA.