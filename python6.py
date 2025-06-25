numero_ingresado = int(input("ingrese el numero a sumar: "))
resultado = 0
negativo = False
resultado = 0
while not negativo:
    if numero_ingresado < 0:
        negativo = True
        break
    resultado = resultado + numero_ingresado
    print(f"el resultado es: {resultado}")
    numero_ingresado = int(input("ingrese el numero a sumar: "))