precios = {"manzana": 2, "naranja": 1.5, "plantano": 4, "piña": 3}
while True:
    fruta = input("Dime la fruta que as vendido: ")
    if fruta.lower() not in precios:
        print("Fruta no existe")
    else:
        cantidad = int(input("Dime la cantidad que has venido"))
        print("El precio es de %f" % (cantidad * precios[fruta]))
    opcion = input("¿Quieres vender otra fruta? (s/n)")
    while opcion.lower() != "s" and opcion.lower() != "n":
        opcion = input("¿Quieres vender otra fruta? (s/n)")
    if opcion.lower() == "n":
        break
