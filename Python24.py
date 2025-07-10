cantidad = 0
nombre = ""
año = ""

def guardar(peliculas):
    cantidad = int(input("\nIngrese la cantidad de peliculas a guardar: "))
    for i in range(1,cantidad+1):
        print(f"-----------Guardar {i} Pelicula--------------")
        nombre = input("Ingrese el nombre de la pelicula: ").lower()
        año = int(input("Ingrese el año de estreno: "))
        
        peliculas.append({
            "nombre": nombre,
            "año": año
        })

def eliminar(peliculas):
    pelis = []
    nombre_a_eliminar = input("\nIngrese el nombre de la pelicula a eliminar: ").lower()
    for indice,pelicula in enumerate(peliculas):
        if pelicula["nombre"] == nombre_a_eliminar:
            encontrado = True
            peliculas.pop(indice)


def buscar(peliculas):
    nombre_a_buscar = input("\nIngrese el nombre de la pelicula a buscar: ").lower()
    for pelicula in peliculas:
        if pelicula["nombre"] == nombre_a_buscar:
            encontrado = True
            print("Pelicula encontrada: ")
            print(f"{pelicula["nombre"]} - {pelicula["año"]}")

def mostrar(peliculas):
    for indice,pelicula in enumerate(peliculas):
        print(f"{indice+1} - {pelicula["nombre"]} - {pelicula["año"]}")

def menu():
    print("-----Tienda de peliculas----")
    print("1. Guardar")
    print("2. Mostrar")
    print("3. Eliminar")
    print("4. Buscar")
    print("5. Salir")