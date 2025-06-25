def veterinario():

 mascotas = 3

while True:
    print("--- Bienvenidos al sistema de la veterania patuelli ----")
    print("seleccione una opcion:")
    print("1. mascotas")
    print("2. salir")
    
    opcion = input("ingrese una opcion: (1-2): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la mascota: ")
        edad = int(input("ingrese la edad de la mascota: "))
        print(f"el nombre de la mascota es: {nombre}")
        print(f"la edad de {nombre} es {edad} años")

        if edad <= 1:
           print(f"la mascota {nombre} debe recibir su vacuna de los parasitos")
           respuesta = input(f"desea administrar la vacuna correspondiente a {nombre} (si/no): ")

           if respuesta == "si":
              print("la vacuna antiparasitaria a sido administrada.")
           elif respuesta == "no":
              print("advertencia debe administar la vacuna correspondiente")

        elif edad > 1 and edad < 3:
           print(f"la mascota {nombre} debe vacunarse contra la influenza")
           respuesta = input(f"desea vacunar administrar la vacuna antifluenza a {nombre} (si/no): ")

           if respuesta == "si":
              print("la vacuna antifluenza fue administrada")
           elif respuesta == "no":
              print("Advertencia, se debe administrar la vacuna a tu mascota")
        break
    
    elif opcion == "2":
      print("saliendo del porgrama")
      break
    
    else:
       print("opcion no valida, selecione una opcion valida")
                         
veterinario()