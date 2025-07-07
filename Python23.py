peliculas = []

#elicula = input("Ingrese el nombre de la película: ")

cantidad = int(input("Ingrese la cantidad de películas a guardar: "))

for i in range(1, cantidad + 1):
    nombre= input(f"Ingrese el nombre de la película {i}: ").lower()
    tipo = input("Ingrese el tipo de la película : ").lower()
    publicacion = input("Ingrese la fecha de publicación de la película: ")

    pelicula = {
        "id": i,
        "nombre": nombre,
        "tipo": tipo,
        "publicacion": publicacion
    }
    peliculas.append(pelicula)

for peli in peliculas:
    print(f"el id es: {peli['id']}")
    print(f"el nombre de la pelicula es: {peli['nombre']}")
    print(f"el tipo de la película es: {peli['tipo']}")
    print(f"la fecha de publicación de la película es: {peli['publicacion']}")

#eliculas.apped(pelicula)



#for pelicula in peliculas:
#    print(f"El nombre de la pelicula es: {pelicula}")