personas={}

def agregar_persona(nombre,mayor_edad):
    personas[nombre]=[mayor_edad]

    for i,j in personas.items():
        print("Persona :",i)
        print("Mayor de edad :",j[0])


while True:
    print("*** Menu ***")
    print("1. Agregar persona")
    print("2. Mostrar una persona")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion : "))

    if(opcion == 1):
        
        nombre_persona = input("Ingrese nombre persona : ")
        
        while True:
            mayor_edad = input("¿Es mayor de edad? (S/N): ")
            if mayor_edad.upper() == "S" or mayor_edad.upper() == "N":
                break
            else:
             print("debe ingresar S o N solamente.")

        agregar_persona(nombre_persona,mayor_edad)     

    elif(opcion == 2):    
        print("Opcion 1")
    elif(opcion == 3):
        print("Salir")
        break
    else:
        print("Opcion no valida")   