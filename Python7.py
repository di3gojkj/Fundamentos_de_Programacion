def calcular_digito_verificador(rut): #hecho por mi
    multiplicadores = [2, 3, 4, 5, 6, 7]
    rut_invertido = str(rut)[::-1]

    suma = 0
    for i in range(len(rut_invertido)):
        suma += int(rut_invertido[i]) * multiplicadores[i % 6]

    resta = suma % 11
    digito = 11 - resta

    if digito == 11:
        return "0"
    elif digito == 10:
        return "K"
    else:
        return str(digito)


print("verificador de RUT")
print("===================")

while True:
    entrada = input("Ingrese el RUT (sin puntos ni dígito verificador): ")
    if entrada.lower() == "salir":
        break
    rut = entrada.replace(".", "")
    if not rut.isdigit():
        print("RUT inválido, por favor ingrese un RUT válido.")
        continue
    dv = calcular_digito_verificador(rut)
    print(f"El dígito verificador para el RUT {rut} es: {dv}")
    print(f"RUT completo: {rut}-{dv}")