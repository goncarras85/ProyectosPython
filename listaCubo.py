import random
lista_numeros = []
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))
for num in lista_numeros:
    print(num, " ", num ** 2, " ", num ** 3)
