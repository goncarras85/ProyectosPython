def EsBisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def DiasDelMes(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if EsBisiesto(year):
            return 29
        else:
            return 28

def Calcular_Dia_Juliano(day,month,year):
    diaj = 0
    for mes in range (1,month):
        diaj = diaj + DiasDelMes(mes,year)
    diaj = diaj + day
    return diaj

def LeerFecha():
    day = int(input("Introduce el dia: "))
    month= int(input("Introduce el mes: "))
    year = int(input("Introduce el año: "))
    return day, month, year

d,m,a = LeerFecha()
print("Dia Juliano: ", Calcular_Dia_Juliano(d,m,a))