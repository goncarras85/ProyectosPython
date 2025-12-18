num = 1
cantidad = int(input("Ingrese un número para calcular su factorial: "))
contador = 2
resultado = 1

for i in range(1, cantidad + 1):
    num = num * i

print("Hecho con For: ")

print("El resultado del factorial de", cantidad, "es:", num )

print("Hecho con While: ")

while(contador <= cantidad):
    resultado = resultado * contador
    contador += 1
    
print("El resultado del factorial de", cantidad, "es:", resultado )
