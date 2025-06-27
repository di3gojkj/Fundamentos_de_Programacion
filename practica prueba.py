pokemones = []
tipos = ["fuego","agua", "hierba", "veneno", "psiquico", "luchador","electrico"]

while True:
    print("MENU PRINCIPAL")
    print("1.- Ingresar pokemon")
    print("2.- Buscar pokemon")
    print("3.- Eliminar pokemon")
    print("4.- Listar pokemones")
    print("5.- Salir")

    opcion = int(input("Ingrese opcion: (1-5) "))

    if opcion == 1:
        pokid = int(input("Ingrese el Id del pokemon: "))
        name = input("Ingrese el nombre de pokemon: ")
        codigo = input("Ingrese código: ")
        tipos = input("Ingrese tipo: ").strip().lower() #.strip() remueve espacios ,lower() convierte a minúsculas
        

        while tipos not in ["fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "electrico"]:
            print("Debe ingresar: “fuego”, “agua”,” hierba”,” veneno”,” psíquico”,”luchador”,”electrico”.")
            tipos = input("Ingrese tipo: ").strip().lower() #.strip() remueve espacios ,lower() convierte a minúsculas
            
        pokemones.append({#. append agrega un nuevo elemento al final de la lista
        "id": pokid,
        "nombre": name,
        "codigo": codigo,
        "tipos": tipos
        })
        print("Pokemon ingresado con éxito!")

    elif opcion == 2:
        nombre = input("Ingrese pokemon a buscar:").strip().lower()
        for p in pokemones:
            if p["nombre"] == nombre:
                print(f"El tipo del pokemon es: {tipos} y su código es : {codigo}")
            else:
                print("Pokemon no encontrado")

    elif opcion == 3:
        nombre = input("Ingrese pokemon a eliminar: ")
        for i,p in enumerate(pokemones):
            if p["nombre"] == nombre:
                del pokemones[i]
                print("Pokemon eliminado con éxito")
            else:
                print("No se pudo eliminar pokemon!")

    elif opcion == 4:
        if not pokemones:
            print("No hay pokemones")
        else:
            print("Lista de pokemones: ")
            for p in pokemones:
                print(f"ID:{p['id']}, Nombre: {p['nombre']}, Tipo: {p['tipos']}")

    elif opcion == 5:
        print("Saliendo...")
        break
    
    else:
        print("opcion no valida, Ingrese una opcion valida (1-5)")
        continue
