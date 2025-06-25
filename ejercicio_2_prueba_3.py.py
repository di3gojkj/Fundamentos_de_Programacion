def cine():
    entradas = 20

    while True:
        print("---Bienvendio al cine estrella---")
        print("1. ver cuantas entradas quedan disponibles")
        print("2. compra de entradas")
        print("3. salir del sistema")
    
        opcion = int(input("ingrese una de las opciopnes (1-3): "))
    
        if opcion == 1:
            print(f"Las entradas disponibles son: {entradas}")
        
        elif opcion == 2:
            try:
                contador_de_compras = int(input("¿Cuantas entradas desea comprar?"))
                entradas = entradas - contador_de_compras
                if contador_de_compras <= entradas:
                    print(f"compra exitosa. quedan {entradas} entradas")
                else:
                    print(f"entradas disponibles insuficiente para la compra, quedan {entradas} entradas")
            except ValueError:
                print("Error: se debe ingresar un numero entero, intente nuevamente.")
                
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, ingrese una opcion no valida")
        
            
cine()