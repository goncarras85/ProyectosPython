tabla = []
for indice_fila in range (1,6):
    fila = []
    for indice_col in range (1,6):
        fila.append(int(input("Intrduce el numero de la fila %d y columna %d: " % (indice_fila, indice_col))))
    tabla.append(fila)

indice_fila = 1
for fila in tabla:
    print("La suma de los elementos de la fila %d es %d" % (indice_fila, sum(fila)))
    indice_fila += 1

for indice_col in range (1,6):
    suma = 0
    for fila in tabla:
        suma += fila[indice_col - 1]
    print("La suma de los elementos de la columna %d es %d" % (indice_col, suma))

