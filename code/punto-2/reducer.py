#!/usr/bin/env python
"""reducer.py"""

import sys
import pdb

f_ventas_sorted = open("code/punto-2/f_ventas_sorted.txt")
f_ventas_result = open("code/punto-2/f_ventas_result_1.txt", "w")

current_vendedor = None
current_count = 0
vendedor = None

for line in f_ventas_sorted:

    line = line.strip()

    id_coordinador, id_vendedor, cant_prod_vendidos = line.split('\t')

    try:
        cant_prod_vendidos = int(cant_prod_vendidos)
    except ValueError:
        continue

    if current_vendedor == id_vendedor:
        current_count += cant_prod_vendidos
    else:
        # pdb.set_trace()
        if current_vendedor:
            f_ventas_result.write(current_coordinador + "\t" + current_vendedor + "\t" + str(current_count) + "\n")
        current_count = cant_prod_vendidos
        current_coordinador = id_coordinador
        current_vendedor = id_vendedor

if current_vendedor == id_vendedor:
    f_ventas_result.write(current_coordinador + "\t" + current_vendedor + "\t" + str(current_count) + "\n")