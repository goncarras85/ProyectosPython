cadena = input("Introduce una cadena de texto: ")
subcadena = input("Introduce una subcadena: ")

if cadena.startswith(subcadena):
    print("La cadena empieza por la subcadena")
else:
    print("La cadena no empieza por la subcadena")