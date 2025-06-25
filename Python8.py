def validar_Rut(rut): #lo hizo el profe lol
    mult = 2
    num = 0
    total = 0
    suma_total = 0
    resto = 0
    resultado = 0

    for caracter in reversed(rut):
        num = int(caracter)
        total = num * mult
        mult += 1

        if mult > 7:
            mult = 2

        suma_total = suma_total + total

    total1 = suma_total // 11 # Dividir 11
    total2 = suma_total % 11 # El residuo de la división por 11
    total3 = total1 * 11 # El resultado de la división por 11 multiplicado por 11
    total4 = suma_total - total3 # A la suma le resto el paso anterior

    dv = 11 - total4 # A 11 le resto el resultado

    if dv == 11:
        dv = 0
        return f"{rut}-{str(dv)}"

    elif dv == 10:
        dv = "k"
        return f"{rut}-{str(dv)}"

    else:
        return f"{rut}-{str(dv)}"

