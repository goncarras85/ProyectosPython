es_Primo = True
num = int(input("Ingrese un numero para saber si es primo: "))
for i in range(2, num):
    if num % i == 0:
        es_Primo = False
        break
if es_Primo:
    print("Es primo")
else:
    print("No es primo")