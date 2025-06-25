def banco():
    print("Bienvenido al banco de la nacion")
    print("menu de opciones")
    print("1. Ingrese el monto a pagar de la tarjeta de credito")
    print("2. ingrese articulo a comprar")
    print("3. salir")

    saldo_inicial = 500_000
    monto = 0
    deuda = 100_000


    while True:
        try:
            opcion = int(input("Por favor eliga una opcion: "))
        
            if opcion == 1:
                print(f"Su saldo es: ${saldo_inicial}")
                print(f"Su deuda es: ${deuda}")
            
                respuesta = input("Desea pagar la deuda? (si/no): ")
            
                if respuesta == "si":
                    print("Por favor ingrese el monto a pagar")
                    monto = int(input("Ingrese Monto a pagar: $"))
        
                    if monto <= saldo_inicial and monto <= deuda and monto > 0:
                        saldo_inicial -= monto
                        deuda -= monto
                        print(f"Pago realizado. Su Saldo actual es de: ${saldo_inicial}")
                        print(f"Su deuda restante es: ${deuda}")
                    else:
                        print("Monto inválido o insuficiente")
                else:
                    print("No se realizo el pago")
                    break
        except ValueError:
                    print("Error: ingrese un monto en numero entero")
                
        if opcion == 2:
                print("=== SIMULACIÓN DE COMPRAS ===")
                print(f"Su saldo actual es: ${saldo_inicial}")
            
                total_compras = 0
                numero_compras = 0
            
                while True:
                    try:
                        respuesta = input("¿Desea realizar una compra? (si/no): ")
                
                        if respuesta == "si":
                            monto_compra = int(input("Ingrese el monto de la compra: $"))
                    
                            if monto_compra > 0:
                                if monto_compra <= saldo_inicial:
                                    saldo_inicial -= monto_compra
                                    total_compras += monto_compra
                                    numero_compras += 1
                                    print(f"Compra {numero_compras} realizada por ${monto_compra}")
                                    print(f"Saldo restante: ${saldo_inicial}")
                                    print(f"Total gastado: ${total_compras}")
                                else:
                                    print("Saldo insuficiente para esta compra")
                        else:
                            print("No se realizaron compras")
                            break
                    except ValueError:
                         print("Error: Ingrese solo numeros enteros.")
        
        elif opcion == 3:
                print("Hasta luego, vuelva pronto!")
                break
        else:
             print("opcion no valida")
             
                
banco()