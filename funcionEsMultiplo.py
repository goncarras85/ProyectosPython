def esmultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
if esmultiplo(numero1, numero2):
    print(numero1, "es multiplo de", numero2)
else:
    print(numero1, "no es multiplo de", numero2)