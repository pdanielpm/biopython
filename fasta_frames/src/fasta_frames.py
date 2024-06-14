'''
NAME
  FASTA_FRAMES

VERSION
    1.0

AUTHOR
    Pedro Pineda    

DESCRIPTION
    Programa que extrae los codones de una secuencia de ADN en los seis marcos de lectura y los guarda en archivos en formato FASTA.
        

CATEGORY
    Secuencias de ADN


USAGE
    python fasta_frames.py archivo.fasta

ARGUMENTS
    archivo.fasta: Archivo en formato FASTA con la secuencia de ADN de la cual se extraerán los codones.



SEE ALSO
        
'''

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse
from Bio.Seq import Seq
from Bio import SeqIO

# ===========================================================================
# =                            functions
# ===========================================================================

def extract_codons(frame, sequence, output_filename):
    """
    Extrae codones de una secuencia de ADN en un marco de lectura específico y los guarda en un archivo en formato FASTA.
    
    :param frame: Marco de lectura (0, 1, 2 para la cadena directa, 3, 4, 5 para la cadena complementaria)
    :param sequence: Secuencia de ADN
    :param output_filename: Nombre del archivo de salida
    """
    if frame >= 3:
        sequence = sequence.reverse_complement()
        frame -= 3

    # Ajustar la secuencia al marco de lectura específico
    codons = [str(sequence[i:i+3]) for i in range(frame, len(sequence) - 2, 3)]
    codon_str = ' '.join(codons)
    
    with open(output_filename, 'w') as file:
        file.write(f">{output_filename}\n{codon_str}\n")


# ===========================================================================
# =                            main
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(description="Extrae codones de los 6 marcos de lectura de una secuencia de ADN.")
    parser.add_argument("input_file", help="Ruta al archivo de entrada con la secuencia de ADN en formato FASTA.")
    
    args = parser.parse_args()
    
    # Leer la secuencia de ADN desde el archivo
    record = SeqIO.read(args.input_file, "fasta")
    sequence = record.seq
    
    for frame in range(6):
        output_filename = f"Frame{frame+1}.fasta"
        extract_codons(frame, sequence, output_filename)
        print(f"Codones del Frame {frame+1} guardados en {output_filename}")

if __name__ == "__main__":
    main()
