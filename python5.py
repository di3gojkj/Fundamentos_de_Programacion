print("1.Sumar")
print("2.Restar") 
print("3.Multiplicar")
print("4.Dividir")
print("5.Salir")

opcion = 0
valor_1 = 0
valor_2 = 0
resultado = 0  

while opcion < 5:
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        resultado = valor_1 + valor_2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        resultado = valor_1 - valor_2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        resultado = valor_1 * valor_2
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == 4:
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        resultado = valor_1 / valor_2
        print(f"El resultado de la division es: {resultado}")
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, por favor ingrese una opcion correcta.")