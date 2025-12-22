while True:
    try:
        x = int(input("Introduce un número: "))
        break
    except ValueError:
        print ("Debes introducir un número")
