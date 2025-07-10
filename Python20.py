personas = []

def agregar_persona():
    cantidad = int(input("\nIngrese la cantidad de personas que desea agregar: "))
    for i in range(1, cantidad + 1):
        print(f"\n-----------Guardar {i} personas--------------")
        nombre = input("Ingrese el nombre de la persona: ").lower()
        mayor_edad = input("¿Es mayor de edad? (Si/No): ").lower()
        if mayor_edad == "si":
            mayor_edad = True
        elif mayor_edad == "no":
            mayor_edad = False
        
        personas.append({
            "nombre": nombre,
            "mayor_edad": mayor_edad
        })

def mostrar_persona():
    if not personas:
        print("No hay personas registradas con ese nombre.")
    for indice, persona in enumerate(personas):
        print(f"{indice+1} - {persona['nombre']} - {'Mayor de edad' if persona['mayor_edad'] else 'Menor de edad'}")

while True:
    print("\n*** Menu ***")
    print("1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion : "))

    if opcion == 1:
        agregar_persona()
    elif opcion == 2:
        mostrar_persona()
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intente nuevamente.")
        continue
