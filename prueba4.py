n_usuario = []


def usuario():
    name = input("Ingrese nombre de usuario: ").lower()
    sexo = input("Ingrese Sexo (F/M): ").lower()
    while sexo not in ["f", "m"]:
        print("Debe ingresar sexo correcto")
        sexo = input("Ingrese Sexo (F/M): ").lower()

    while True:
        contraseña = input("Ingrese Contraseña: ").strip()
        if (len(contraseña) == 8 and
            any(c.isupper() for c in contraseña) and
            any(c.isdigit() for c in contraseña)):
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta. Debe tener exactamente 8 caracteres, al menos una mayúscula y al menos un número.")

    n_usuario.append({
        "nombre": name,
        "sexo": sexo,
        "contraseña": contraseña,
    })
    print("Usuario ingresado con éxito!")

def usuario_a_buscar():
    nombre = input("Ingrese usuario a buscar:").lower()
    for n in n_usuario:
        if n["nombre"] == nombre:
            print(f"\nEl sexo del usuario es: {n['sexo']} y su contraseña es : {n['contraseña']}")
        else:
            print("\nusario no encontrado")

def usuario_a_eliminar():
    nombre = input("Ingrese usuario a eliminar: ").lower()
    for i,n in enumerate(n_usuario):
        if n["nombre"] == nombre:
            del n_usuario[i]
            print("\nusuario eliminado con éxito")
        else:
            print("No se pudo eliminar el usuario (usuario no encontrado)!")       



    

while True:
    print("\nMENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

    opcion = int(input("\nIngrese una opcion (1-4): "))

    if opcion == 1:
        usuario()

    elif opcion == 2:
        usuario_a_buscar()
        
    elif opcion == 3:
        usuario_a_eliminar()
           
    elif opcion == 4:
        print("Saliendo del Programa... ")     
        break

    else:
        print("\nOpcion invalida, ingrese una opcion correcta (1-4) ")
        continue






