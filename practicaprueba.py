#pokemon = {
    #"01": ["Pikachu", "04k5", "Electrico"],
    #"02": ["Bulbasur", "06j3", "Hierba"],
    #"03": ["Charizard", "02l9", "Fuego"],
    #"05": ["squartle", "08m9", "Agua"],
    #"06": ["Drapion", "26r9", "Veneno"],
    #"07": ["Alakazam", "64r87", "Psiquico"],
    #"08": ["Machamp", "57g4", "Luchador"],
#}
id_pokemon = 0
n_pokemon = 0
codigo_pokemon = 0
tipo = ["electrico", "hierba", "fuego", "agua", "veneno","psiquico", "luchador"]

def ingresar_pokemon():
    id_pokemon = int(input("Ingrese el Id de Pokemon: "))
    n_pokemon = input("Igrese nombre de pokemon: ")
    codigo_pokemon = float(input("Ingrese codigo: "))
    Tipo = int(input("ingrese Tipo: "))








while True:
    print("MENU PRINCIPAL")
    print("1. Ingresar Pokemon")
    print("2. Buscar Pokemon")
    print("3. Eliminar Pokemon")
    print("4. Listar Pokmones")
    print("5. Salir")

    opcion = input("Ingrese una opcion (1-5): ")

    if opcion == "1":
        ingresar_pokemon()
    
    #elif opcion == "2":

    #elif opcion == "3":

    #elif opcion == "4":

    #elif opcion =="5":
        #print("Saliendo del programa...")
        #break
    #else:
        #print("Opcion invalida, Seleccione una opcion correcta (1-5)")
        #continue