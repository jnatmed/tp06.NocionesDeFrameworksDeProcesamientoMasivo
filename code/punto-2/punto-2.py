#!/usr/bin/env python
"""punto-1.py"""

import sys

# Abro el archivo ventas.txt
file_hdfs = open("code/punto-1/ventas.txt")

# Declaro los diccionarios
lista_vendedores = {}
lista_coordinadores = {}
lista_cant_ventas = {}

# Leo cada linea del archivo ventas.txt
for line in file_hdfs:

    # Se eliminan los espacios en blanco iniciales y finales
    line = line.strip()

    # cada linea tiene exactamente 4 palabras
    (id_vendedor, id_coordinador, cant_prod_vendidos, total_venta) = line.split("\t")

    # convierto a entero los valores de:
    #      id_vendedor, 
    #      id_coordinador y 
    #      cantidad productos vendidos
    id_vendedor = int(id_vendedor)
    id_coordinador = int(id_coordinador)
    cant_prod_vendidos = int(cant_prod_vendidos)
    # total venta va a dar en coma flotante, entonces: 
    #       1° lo paso a float
    #       2° lo paso a entero 
    total_venta = int(float(total_venta))

    # voy sumando el total de dinero vendido por vendedor <-- PUNTO a)
    # voy sumando la cantidad vendida por vendedor <-- PUNTO b)
    if id_vendedor in lista_vendedores:
        lista_vendedores[id_vendedor] = lista_vendedores[id_vendedor] + total_venta
        lista_cant_ventas[id_vendedor] = lista_cant_ventas[id_vendedor] + cant_prod_vendidos
    else:
        lista_vendedores[id_vendedor] = total_venta  
        lista_cant_ventas[id_vendedor] = cant_prod_vendidos

    
    # voy guardando los vendedores por coordinador
    if id_coordinador in lista_coordinadores:
        lista_coordinadores[id_coordinador].append(id_vendedor)
    else:
        lista_coordinadores[id_coordinador] = [id_vendedor]


# creo los archivos de informes resultantes 
# f_ventas_por_vendedor: 
#       - PUNTO a) total dinero vendido por vendedor y el bonus
# f_cant_ventas_por_vendedor_por_coordinador: 
#       - PUNTO b) total ventas realizadas por vendedor por coordinador                
# f_lista_coordinadores: 
#       - listado de coordinadores        
f_ventas_por_vendedor = open("code/punto-1/f_ventas_por_vendedor.txt", "w")
f_cant_ventas_por_vendedor = open("code/punto-1/f_cant_ventas_por_vendedor_por_coordinador.txt", "w")
f_lista_coordinadores = open("code/punto-1/f_lista_coordinadores.txt", "w")

# ordeno el listado de vendedores y el listado de coordinadores
lista_vendedores_ordenada = sorted(lista_vendedores.items(), key=lambda x:x[0])
lista_coordinadores_ordenada = sorted(lista_coordinadores.items(), key=lambda x:x[0])

# escribo en el informe de salida: "f_lista_coordinadores"
#       - titulo: "lista de coordinadores"
f_ventas_por_vendedor.write("**********\n")
f_ventas_por_vendedor.write("LISTA VENDEDORES\n")
f_ventas_por_vendedor.write("ID_VENDEDOR | ID_COORDINADOR | BONUS\n\n")


# recorro la lista de vendedores ORDENADA
for id,value in lista_vendedores_ordenada:

    # multiplico el total vendido por el 3% para obtener el bonus
    bonus = value * 0.03

    # escribo en el informe de salida: "f_ventas_por_vendedor" <-- PUNTO a)
    #       - el id de vendedor
    #       - la cantidad de dinero vendida
    #       - el bonus (3%)
    f_ventas_por_vendedor.write(str(id)+"\t\t"+str(lista_vendedores[id])+"\t"+str(bonus)+"\n")


# escribo en el informe de salida: "f_cant_ventas_por_vendedor" <-- PUNTO b)
#       - cantidad de coordinadores totales
f_cant_ventas_por_vendedor.write("Cantidad Coordinadores: " + str(len(lista_coordinadores_ordenada))+"\n")

# escribo en el informe de salida: "f_lista_coordinadores"
#       - titulo: "lista de coordinadores"
f_lista_coordinadores.write("**********\n")
f_lista_coordinadores.write("LISTA COORDINADORES\n")
f_lista_coordinadores.write("ID_COORDINADOR\n\n")


# recorro la lista de coordinadores ORDENADA
for coordinador, vendedores in lista_coordinadores_ordenada:

    # escribo en el informe de salida: "f_cant_ventas_por_vendedor" <-- PUNTO b)
    #           - id coordinador
    #           - cantidad de vendedores asignados
    f_cant_ventas_por_vendedor.write("**************************\n")
    f_cant_ventas_por_vendedor.write("ID Coordinador -> " + str(coordinador) + "\n")
    f_cant_ventas_por_vendedor.write("Cantidad de Vendedores Asignados: "+ str(len(vendedores))+"\n")
    f_cant_ventas_por_vendedor.write("ID_VENDEDOR | CANT_VENTAS\n")
    f_cant_ventas_por_vendedor.write("------ | ------ |\n")

    # escribo en el informe de salida: "f_lista_coordinadores"
    #           - el id del coordinador
    f_lista_coordinadores.write(str(coordinador)+"\n")

    # escribo en el informe de salida: "f_cant_ventas_por_vendedor" <-- PUNTO b)
    for v in vendedores:

        # escribo por vendedor
        # - id vendedor
        # - cantidad vendida
        cant_ventas = lista_cant_ventas[v]    
        f_cant_ventas_por_vendedor.write(str(v) + "\t|\t" + str(cant_ventas) + "\n")

# Finalizo cerrando todos los archivos.

file_hdfs.close()
f_ventas_por_vendedor.close()
f_lista_coordinadores.close()
f_cant_ventas_por_vendedor.close()

# Fin programa.