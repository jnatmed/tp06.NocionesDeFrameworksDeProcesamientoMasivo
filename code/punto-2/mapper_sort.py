#!/usr/bin/env python
"""mapper_sort.py"""

import sys
import pdb

def convertir_id(line):
    line = line.strip()
    linea_split = []
    linea_split = line.split("\t") 
    # PARTE IMPORTANTE DEL SORT, SELECCIONO LA COLUMNA POR LA CUAL
    # QUIERO ORDENAR, EN ESTE CASO COLUMNA ID_VENDEDOR
    # PARA DESPUES HACER EL ACUMULADOR DE CANT_VENTAS_REALIZADAS 
    return int(linea_split[1])

# Abro el archivo ventas_part1.txt
file_hdfs = open("code/punto-2/f_ventas_part1.txt")

f_vendedor_ventas = open("code/punto-2/f_ventas_sorted.txt", "w")

for line in sorted(file_hdfs, key=convertir_id):
    f_vendedor_ventas.write(line)

file_hdfs.close()
f_vendedor_ventas.close()

# Fin programa.