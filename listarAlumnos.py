nombres = []
edades = []
while True:
    nombre = input("Introduce un nombre: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Introduce edad: ")))
    if nombre == "*":
        break;
edad_max = max(edades)
print("Alumnos mayores de edad")
print("=======================")
for nombre, edad in zip(nombres,edades):
    if edad >= 18:
        print(nombre)

print("Alumnos mayores")
print("===============")
for nombre, edad in zip(nombres,edades):
    if edad == edad_max:
        print(nombre)