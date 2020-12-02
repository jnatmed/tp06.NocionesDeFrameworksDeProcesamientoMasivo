#!/usr/bin/env python
"""reducer_sort.py"""

import sys


def convertir_id(line):
    line = line.strip()
    linea_split = []
    linea_split = line.split("\t")    
    return int(linea_split[0])

# Abro el archivo ventas_part1.txt
file_hdfs = open("code/punto-2/f_ventas_result_1.txt")

f_vendedor_ventas = open("code/punto-2/f_reducer_sorted.txt", "w")

for line in sorted(file_hdfs, key=convertir_id):
    f_vendedor_ventas.write(line)

file_hdfs.close()
f_vendedor_ventas.close()

# Fin programa.