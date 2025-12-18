num = int(input("Ponme un numero para ver su tabla de multiplicar: "))
for i in range (0, 11):
    resultado = 0
    resultado = num * i
    print(num, "x", i, "=", resultado)