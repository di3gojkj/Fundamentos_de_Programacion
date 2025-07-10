from Python24 import guardar,mostrar,menu,buscar,eliminar
peliculas = []
encontrado = False
while True:
    try:
        menu()
        opt = int(input("\nIngrese la opcion: "))
        if opt == 1:        
            guardar(peliculas)
            print("Peliculas guardadas exitosamente!!!!")        
        elif opt == 2:
            mostrar(peliculas)        
        elif opt == 3:
            eliminar(peliculas)
        elif opt == 4:
            buscar(peliculas)
        elif opt == 5:
            break
    except ValueError:
        print("Solo valores numericos")


print("Gracias, vuelva pronto")