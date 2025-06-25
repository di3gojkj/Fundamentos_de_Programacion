valor_1 = 0
valor_2 = 0
resultado = 0

def suma():
    print("\n--- Estas Sumando ---")

    valor_1 = int(input("\nIngrese el primer valor: "))
    valor_2 = int(input("Ingrese el segundo valor: "))
    resultado = valor_1 + valor_2
    print(f"El resultado de la suma es: {resultado}")

def resta():
    print("--- Estas Restando ---")

    valor_1 = int(input("Ingresa el primer valor: "))
    valor_2 = int(input("Ingresa el segundo valor: "))
    resultado = valor_1 - valor_2
    print(f"El resultado es: {resultado}")

def multiplo():
    Print("--- Estas multiplicando ---")

    valor_1 = int(input("Ingrese el primer valor: "))
    valor_2 = int(input("Ingrese el segundo valor: "))
    resultado = valor_1 * valor_2
    print(f"El resultado es: {resultado}")

def divisor():
    print("--- Estas dividiendo ---")

    valor_1 = int(input("Ingrese el primer valor: "))
    valor_2 = int(input("Ingrese le segundo valor: "))
    resultado = valor_1 / valor_2
    print(f"El resultado es: {resultado}")


        


while True:
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")

    opcion = input("Ingrese una opcion (1-5): ")
    if opcion == "1":
        suma()
    elif opcion == "2":
        resta()
    elif opcion == "3":
        multiplo()
    elif opcion == "4":
        divisor()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opcion valida...")
        continue

