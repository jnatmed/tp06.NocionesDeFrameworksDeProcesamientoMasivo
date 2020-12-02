#!/usr/bin/env python
"""reducer.py"""

import sys

f_ventas_sorted = open("code/punto-1/f_ventas_sorted.txt")
f_ventas_result = open("code/punto-1/f_ventas_result.txt", "w")

current_vendedor = None
current_count = 0
vendedor = None

for line in f_ventas_sorted:

    line = line.strip()

    id_vendedor, dinero_venta = line.split('\t', 1)

    try:
        dinero_venta = int(float(dinero_venta))
    except ValueError:
        continue

    if current_vendedor == id_vendedor:
        current_count += dinero_venta
    else:
        if current_vendedor:
            bonus = current_count * 0.03
            f_ventas_result.write(current_vendedor + "\t" + str(current_count) + "\t" + str(bonus) +"\n")
        current_count = dinero_venta
        current_vendedor = id_vendedor

if current_vendedor == id_vendedor:
    f_ventas_result.write(current_vendedor + "\t" + str(current_count) + "\t" + str(bonus) +"\n")