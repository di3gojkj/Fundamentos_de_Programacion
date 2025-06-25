saldo = 100000

while True:
    print("\n Bienvenido al banco del pais, selecione una opcion.")
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. salir")

    opcion = input("\n selecione una opcion (1-3):")
    
    if opcion == "1":
       print(f"tu saldo actual: ${saldo}")
    elif opcion == "2":
       cantidad_Retiro = int(input("ingrese la cantidad a retirar: $"))
       if cantidad_Retiro <= saldo:
             saldo -= cantidad_Retiro
             print(f"has retirado ${cantidad_Retiro}. nuevo saldo: ${saldo}")
    elif opcion == "3":
      print("gracias por utilizar el cajero.")
      break
    else:
       print("opcion no valida. por favor, seleciona una opcion valida.")