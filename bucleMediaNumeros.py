suma = 0
cont = 0

while True:

    num = int(input("introduzca numeros para calcular su media, introduzca 0 para finalizar : "))
    suma = suma + num
    if num != 0:
        cont += 1
    if num == 0:
        break
if cont != 0:
    media = suma / cont
else:
    media = 0
print("la media de los numeros introducidos es: ", media)