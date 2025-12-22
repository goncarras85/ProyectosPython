cont = 0
posicion = 0
cad = input("Introduce una cadena: ")
cad = cad.strip()
posicion = cad.find(" ", posicion)
while posicion != -1:
    cont += 1
    while cad[posicion + 1] == " ":
        posicion += 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene", cont + 1, "palabras ")