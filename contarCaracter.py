cad = input("Introduce una cadena: ")
while True:
    car = input("Introduce un caracter: ")
    if len(car) == 1:
        break
print("En la cadena", cad, "aparece", cad.count(car), "veces el caracter", car)