#!/usr/bin/env python
"""mapper.py"""

import sys

# Abro el archivo ventas.txt
file_hdfs = open("code/punto-2/ventas.txt")
f_vendedor_ventas = open("code/punto-2/f_ventas_part1.txt", "w")


# Leo cada linea del archivo ventas.txt
for line in file_hdfs:

    # Se eliminan los espacios en blanco iniciales y finales
    line = line.strip()

    # cada linea tiene exactamente 4 palabras
    (id_vendedor, id_coordinador, cant_prod_vendidos, total_venta) = line.split("\t")

    f_vendedor_ventas.write(id_coordinador + "\t" + id_vendedor + "\t" + cant_prod_vendidos + "\n")

file_hdfs.close()
f_vendedor_ventas.close()

# Fin programa.